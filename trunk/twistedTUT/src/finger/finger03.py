#coding=utf-8
'''
    断开连接(Drop Connections)
    现在我们改进了协议(protocol), 使它有能力对建立连接的事件作出反应——断开连接。也许不是一个有趣的做法，但是反应器已经能够根据协议(protocol)来作出反应。毕竟，标准中也没有规定一定要在建立连接的时候向远端发数据。唯一的问题是，我们关闭连接太快。一个很慢的客户端会发现它用send()函数发送用户名时会出现错误。 
'''

from twisted.internet import protocol, reactor
class FingerProtocol(protocol.Protocol):
    def connectionMade(self):
        self.transport.loseConnection()
class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol
reactor.listenTCP(1079, FingerFactory())
reactor.run()
                    