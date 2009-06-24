#coding=utf-8
'''
IWPROXYCLIENT
'''
from collections import deque
from twisted.python.failure import Failure
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.protocols.policies import TimeoutMixin
from twisted.internet.defer import Deferred, fail, TimeoutError
from twisted.python.logfile import LogFile
import datetime

class NoSuchCommand(Exception):
    """
    Exception raised when a non existent command is called.
    """

class ClientError(Exception):
    """
    Error caused by an invalid client call.
    """

class ServerError(Exception):
    """
    Problem happening on the server.
    """

class Command(object):
    """
    Wrap a client action into an object, that holds the values used in the
    protocol.

    @ivar _deferred: the L{Deferred} object that will be fired when the result
        arrives.
    @type _deferred: L{Deferred}

    @ivar command: name of the command sent to the server.
    @type command: C{str}
    """

    def __init__(self, command, **kwargs):
        """
        Create a command.

        @param command: the name of the command.
        @type command: C{str}

        @param kwargs: this values will be stored as attributes of the object
            for future use
        """
        self.command = command
        self._deferred = Deferred()

    def success(self, value):
        """
        Shortcut method to fire the underlying deferred.
        """
        self._deferred.callback(value)

    def fail(self, error):
        """
        Make the underlying deferred fails.
        """
        self._deferred.errback(error)


class PooledIWProxyProtocol(LineReceiver, TimeoutMixin):
    """
    A MemCacheProtocol that will notify a connectionPool that it is ready
    to accept requests.

    @ivar factory: A L{MemCacheClientFactory} instance.
    """
    factory = None
    
    def __init__(self, timeOut=60):
        """
        Create the protocol.
    
        @param timeOut: the timeout to wait before detecting that the
            connection is dead and close it. It's expressed in seconds.
        @type timeOut: C{int}
        """
        self._current = deque()
        self.persistentTimeOut = self.timeOut = timeOut
    
    def connectionMade(self):
        """
        Notify our factory that we're ready to accept connections.
        """
        LineReceiver.connectionMade(self)

        if self.factory.deferred is not None:
            self.factory.deferred.callback(self)
            self.factory.deferred = None
            
    def lineReceived(self, line):
        cmd = self._current.pop()
        cmd.success(line)
            
    def sendLine(self, line):
        """
        Override sendLine to add a timeout to response.
        """
        if not self._current:
           self.setTimeout(self.persistentTimeOut)
        
        LineReceiver.sendLine(self, line)
        
    def method(self, cmd, key):
        if not isinstance(key, str):
            return fail(ClientError("Invalid type for key: %s, expecting a string" % (type(key),)))
        
        fullcmd = "%s %s" % (cmd, key)
        self.sendLine(fullcmd)
        cmdObj = Command(cmd, key=key)
        self._current.append(cmdObj)
        return cmdObj._deferred

class IWProxyClientFactory(ClientFactory):
    """
    A client factory for MemCache that reconnects and notifies a pool of it's
    state.

    @ivar connectionPool: A managing connection pool that we notify of events.
    @ivar deferred: A L{Deferred} that represents the initial connection.
    @ivar _protocolInstance: The current instance of our protocol that we pass
        to our connectionPool.
    """
    protocol = PooledIWProxyProtocol
    connectionPool = None
    _protocolInstance = None


    def __init__(self):
        self.deferred = Deferred()

    def clientConnectionLost(self, connector, reason):
        """
        Notify the connectionPool that we've lost our connection.
        """
        if self._protocolInstance is not None:
            self.connectionPool.clientGone(self._protocolInstance)

    def clientConnectionFailed(self, connector, reason):
        """
        Notify the connectionPool that we're unable to connect
        """
        if self._protocolInstance is not None:
            self.connectionPool.clientGone(self._protocolInstance)
        if self.connectionPool:
            self.connectionPool._pendingConnects -= 1

    def buildProtocol(self, addr):
        """
        Attach the C{self.connectionPool} to the protocol so it can tell it,
        when we've connected.
        """
        if self._protocolInstance is not None:
            self.connectionPool.clientGone(self._protocolInstance)

        self._protocolInstance = self.protocol()
        self._protocolInstance.factory = self
        return self._protocolInstance



class IWProxyPool(object):
    """
    A connection pool for MemCacheProtocol instances.

    @ivar clientFactory: The L{ClientFactory} implementation that will be used
        for each protocol.

    @ivar _maxClients: A C{int} indicating the maximum number of clients.
    @ivar _serverAddress: An L{IAddress} provider indicating the server to
        connect to.  (Only L{IPv4Address} currently supported.)
    @ivar _reactor: The L{IReactorTCP} provider used to initiate new
        connections.

    @ivar _busyClients: A C{set} that contains all currently busy clients.
    @ivar _freeClients: A C{set} that contains all currently free clients.
    @ivar _pendingConnects: A C{int} indicating how many connections are in
        progress.
    """
    clientFactory = IWProxyClientFactory

    def __init__(self, serverAddress, maxClients=5, reactor=None):
        """
        @param serverAddress: An L{IPv4Address} indicating the server to
            connect to.
        @param maxClients: A C{int} indicating the maximum number of clients.
        @param reactor: An L{IReactorTCP{ provider used to initiate new
            connections.
        """
        self._serverAddress = serverAddress
        self._maxClients = maxClients

        if reactor is None:
            from twisted.internet import reactor

        self._reactor = reactor

        self._busyClients = set([])
        self._freeClients = set([])
        self._pendingConnects = 0
        self._commands = []

    def _newClientConnection(self):
        """
        Create a new client connection.

        @return: A L{Deferred} that fires with the L{IProtocol} instance.
        """
        self._pendingConnects += 1

        def _connected(client):
            self._pendingConnects -= 1
            self.clientFree(client)
            return client

        factory = self.clientFactory()
        factory.connectionPool = self
        self._reactor.connectTCP(
            self._serverAddress.host,
            self._serverAddress.port,
            factory,
            timeout=1
        )
        d = factory.deferred
        d.addCallback(_connected)
        return d


    def _performOnClient(self, client, command, *args, **kwargs):
        """
        Perform the given request on the given client.

        @param client: A L{PooledMemCacheProtocol} that will be used to perform
            the given request.

        @param command: A C{str} representing an attribute of
            L{MemCacheProtocol}.
        @parma args: Any positional arguments that should be passed to
            C{command}.
        @param kwargs: Any keyword arguments that should be passed to
            C{command}.

        @return: A L{Deferred} that fires with the result of the given command.
        """
        def _freeClientAfterRequest(result):
            self.clientFree(client)
            return result

        self.clientBusy(client)
        d = client.method(command, *args, **kwargs)
        d.addCallback(_freeClientAfterRequest)
        return d


    def perform(self, command, *args, **kwargs):
        """
        Select an available client and perform the given request on it.

        @param command: A C{str} representing an attribute of
            L{MemCacheProtocol}.
        @parma args: Any positional arguments that should be passed to
            C{command}.
        @param kwargs: Any keyword arguments that should be passed to
            C{command}.

        @return: A L{Deferred} that fires with the result of the given command.
        """
        if len(self._freeClients) > 0:
            client = self._freeClients.pop()

            d = self._performOnClient(
                client, command, *args, **kwargs)

        elif len(self._busyClients) + self._pendingConnects >= self._maxClients:
            d = Deferred()
            self._commands.append((d, command, args, kwargs))

        else:
            self._newClientConnection()
            d = Deferred()
            self._commands.append((d, command, args, kwargs))

        return d

    def clientGone(self, client):
        """
        Notify that the given client is to be removed from the pool completely.

        @param client: An instance of L{PooledMemCacheProtocol}.
        """
        if client in self._busyClients:
            self._busyClients.remove(client)

        elif client in self._freeClients:
            self._freeClients.remove(client)


    def clientBusy(self, client):
        """
        Notify that the given client is being used to complete a request.

        @param client: An instance of C{self.clientFactory}
        """
        if client in self._freeClients:
            self._freeClients.remove(client)

        self._busyClients.add(client)

    def clientFree(self, client):
        """
        Notify that the given client is free to handle more requests.

        @param client: An instance of C{self.clientFactory}
        """ 
        if client in self._busyClients:
            self._busyClients.remove(client)
        self._freeClients.add(client)
        if len(self._commands) > 0:
            d, command, args, kwargs = self._commands.pop(0)
            _ign_d = self.perform(command, *args, **kwargs)
            _ign_d.addCallback(d.callback)
            
    def gpa(self, *args, **kwargs):
        """Get request phone args"""
        return self.perform('gpa', *args, **kwargs)    

class CachePoolUserMixIn(object):
    """
    A mixin that returns a saved cache pool or fetches the default cache pool.

    @ivar _cachePool: A saved cachePool.
    """
    _cachePool = None

    def getCachePool(self):
        if self._cachePool is None:
            return defaultCachePool()
        return self._cachePool

_memCachePool = None

def installPool(serverAddress, maxClients=5, reactor=None):
    global _memCachePool
    _memCachePool = IWProxyPool(serverAddress,
                                 maxClients=maxClients,
                                 reactor=None)

def defaultCachePool():
    return _memCachePool