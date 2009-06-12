#coding=utf-8
'''
    从一个空的工厂(Factory)中输出(Output From Empty Factory)
    这个例子和上面的例子有同样的行为，但是最终我们会看到工厂(Factory)有什么用处：它不需要为每次连接都创建一次，它可以来管理用户数据库。尤其是当后台用户数据库发生了变化时，我们不用改变协议（protocol）。 
'''

# Read username, output from empty factory, drop connections
from twisted.internet import protocol, reactor
from twisted.protocols import basic
class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        self.transport.write(self.factory.getUser(user)+"\r\n")
        self.transport.loseConnection()
class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol
    def getUser(self, user): return "No such user"
reactor.listenTCP(1079, FingerFactory())
reactor.run()
