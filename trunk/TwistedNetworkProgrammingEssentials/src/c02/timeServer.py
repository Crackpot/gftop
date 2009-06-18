import time
import datetime
from twisted.internet import protocol,reactor
class TimeProtocol(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(
            '<META http-equiv=refresh content="1;>\
            Hello.The time is %s'%(datetime.datetime.now())
        )
        self.transport.loseConnection()
class TimeFactory(protocol.ServerFactory):
    protocol=TimeProtocol
reactor.listenTCP(8000,TimeFactory())
reactor.run()
