#!/usr/bin/env python
#coding=utf-8
from twisted.internet import stdio,reactor,protocol
'''
>>> dir(stdio)
['StandardIO', '__builtins__', '__doc__', '__file__', '__name__', 'platform']
>>> dir(protocol)
['AbstractDatagramProtocol', 'BaseProtocol', 'ClientCreator', 'ClientFactory', 'ConnectedDatagramProtocol', 'ConsumerToProtocolAdapter', 'DatagramProtocol', 'Factory', 'FileWrapper', 'ProcessProtocol', 'Protocol', 'ProtocolToConsumerAdapter', 'ReconnectingClientFactory', 'ServerFactory', '_InstanceFactory', '__all__', '__builtins__', '__doc__', '__file__', '__name__', 'components', 'connectionDone', 'defer', 'error', 'failure', 'implements', 'interfaces', 'log', 'random']
>>> dir(basic)
['COMMA', 'DATA', 'DEBUG', 'FileSender', 'Int16StringReceiver', 'Int32StringReceiver', 'Int8StringReceiver', 'IntNStringReceiver', 'LENGTH', 'LineOnlyReceiver', 'LineReceiver', 'NUMBER', 'NetstringParseError', 'NetstringReceiver', 'SafeNetstringReceiver', 'StatefulStringProtocol', 'StringTooLongError', '_PauseableMixin', '__builtins__', '__doc__', '__file__', '__name__', 'defer', 'error', 'implements', 'interfaces', 'log', 'protocol', 're', 'struct']
'''
from twisted.internet import stdio, reactor, protocol
from twisted.protocols import basic
import re
class DataForwardingProtocol(protocol.Protocol):
    def __init__(self):
        self.output = None
        self.normalizeNewlines = False
    def dataReceived(self, data):
        if self.normalizeNewlines:
            data = re.sub(r"(\r\n|\n)", "\r\n", data)
        if self.output:
            self.output.write(data)
class StdioProxyProtocol(DataForwardingProtocol):
    def connectionMade(self):
        inputForwarder = DataForwardingProtocol( )
        inputForwarder.output = self.transport
        inputForwarder.normalizeNewlines = True
        stdioWrapper = stdio.StandardIO(inputForwarder)
        self.output = stdioWrapper
        print "Connected to server.  Press ctrl-C to close connection."
class StdioProxyFactory(protocol.ClientFactory):
    protocol = StdioProxyProtocol
    def clientConnectionLost(self, transport, reason):
        reactor.stop( )
    def clientConnectionFailed(self, transport, reason):
        print reason.getErrorMessage( )
        reactor.stop( )
if __name__ == '__main__':
    import sys
    if not len(sys.argv) == 3:
        print "Usage: %s host port" % __file__
        sys.exit(1)
    reactor.connectTCP(sys.argv[1], int(sys.argv[2]), StdioProxyFactory( ))
    reactor.run( )
