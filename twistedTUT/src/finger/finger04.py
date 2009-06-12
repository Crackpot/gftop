#coding=utf-8
'''
    读用户名，断开连接(Read Username, Drop Connections)
    现在我们从LineReveiver类继承了一个新类叫FingerProtocol， 这样当数据一行一行到达时，就会产生事件，而我们响应事件，然后关闭连接。 
    这是第一个符合finger标准的代码版本。但是，人们通常希望能得到用户的有关信息。 
    
'''

from twisted.internet import protocol, reactor
from twisted.protocols import basic
class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        self.transport.loseConnection()
class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol
reactor.listenTCP(1079, FingerFactory())
reactor.run()
