#coding=utf-8
'''
    从一个非空的工厂(Factory)中输出(Output from Non-empty Factory)
    最终，一个有用的finger数据库出现了。虽然它不能提供登录用户的任何信息，但是可以发布一些类似办公地点，内部办公室编号的信息。就像上面指出的那样，工厂(factory)负责管理用户数据库，而协议(protocol)实例却没有发生改变。这看起来不错，因为我们真的不用老是改协议(protocol)了。 
'''

# Read username, output from non-empty factory, drop connections
from twisted.internet import protocol, reactor
from twisted.protocols import basic
class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        self.transport.write(self.factory.getUser(user)+"\r\n")
        self.transport.loseConnection()
class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol
    def __init__(self, **kwargs): self.users = kwargs
    def getUser(self, user):
        return self.users.get(user, "No such user")
reactor.listenTCP(1079, FingerFactory(moshez='Happy and well'))
reactor.run()