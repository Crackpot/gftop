from twisted.internet import reactor, protocol
'''
>>> dir(protocol)
['AbstractDatagramProtocol', 'BaseProtocol', 'ClientCreator', 'ClientFactory', 'ConnectedDatagramProtocol', 'ConsumerToProtocolAdapter', 'DatagramProtocol', 'Factory', 'FileWrapper', 'ProcessProtocol', 'Protocol', 'ProtocolToConsumerAdapter', 'ReconnectingClientFactory', 'ServerFactory', '_InstanceFactory', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'components', 'connectionDone', 'defer', 'error', 'failure', 'implements', 'interfaces', 'log', 'random']

>>> dir(protocol.Protocol)
['__doc__', '__implemented__', '__module__', '__providedBy__', '__provides__', 'connected', 'connectionLost', 'connectionMade', 'dataReceived', 'makeConnection', 'transport']

>>> dir(protocol.Protocol.transport)
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
'''
class QuickDisconnectProtocol(protocol.Protocol):
    def connectionMade(self):
        print "Connected to %s." % self.transport.getPeer( ).host
        self.transport.loseConnection( )
class BasicClientFactory(protocol.ClientFactory):
    protocol = QuickDisconnectProtocol
    def clientConnectionLost(self, connector, reason):
        print "Lost connection: %s" % reason.getErrorMessage( )
        reactor.stop( )
    def clientConnectionFailed(self, connector, reason):
        print "Connection failed: %s" % reason.getErrorMessage( )
        reactor.stop( )
reactor.connectTCP('www.google.com', 80, BasicClientFactory( ))
reactor.run( )
