#coding=utf-8
'''
    读用户名，输出错误信息，断开连接(Read Username, Output Error, Drop Connections)
    最终我们得到了一个有用的版本。但是这个版本仅仅返回“没有这个用户”的信息，所以不是很有用。当然它也许可以用来搞恶作剧。 
'''

from twisted.internet import protocol, reactor
from twisted.protocols import basic
class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        self.transport.write("No such user\r\n")
        self.transport.loseConnection()
class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol
reactor.listenTCP(1079, FingerFactory())
reactor.run()