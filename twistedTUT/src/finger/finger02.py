#coding=utf-8
'''
    什么也不做(Do Nothing)
    这里，我们开始监听1079端口。1079端口只是临时使用，最终我们会使用79端口，79端口是finger服务器的标准端口。我们定义了一个协议(protocol)，它不响应任何事件。因此可以连接到1079端口，但是任何输入都得不到响应。 
'''

from twisted.internet import protocol, reactor
class FingerProtocol(protocol.Protocol):
    pass
class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol
reactor.listenTCP(1079, FingerFactory())
reactor.run()