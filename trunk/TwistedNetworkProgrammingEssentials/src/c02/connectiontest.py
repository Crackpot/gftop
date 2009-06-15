#!/usr/bin/env python
#coding=utf-8
'''
>>> dir(defer)
['AlreadyCalledError', 'AlreadyTryingToLockError', 'DebugInfo', 'Deferred', 'DeferredFilesystemLock', 'DeferredList', 'DeferredLock', 'DeferredQueue', 'DeferredSemaphore', 'FAILURE', 'FirstError', 'QueueOverflow', 'QueueUnderflow', 'SUCCESS', 'TimeoutError', '_ConcurrencyPrimitive', '_DefGen_Return', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_deferGenerator', '_inlineCallbacks', '_nothing', '_parseDListResult', 'deferredGenerator', 'execute', 'fail', 'failure', 'gatherResults', 'generators', 'getDebugging', 'inlineCallbacks', 'lockfile', 'log', 'logError', 'maybeDeferred', 'mergeFunctionMetadata', 'nested_scopes', 'passthru', 'returnValue', 'setDebugging', 'succeed','timeout', 'traceback', 'unsignedID', 'waitForDeferred', 'warnings']
>>> dir(defer.Deferred)
['__doc__', '__init__', '__module__', '__repr__', '__str__', '_continue', '_debugInfo', '_runCallbacks', '_runningCallbacks', '_startRunCallbacks', 'addBoth', 'addCallback', 'addCallbacks', 'addErrback', 'callback', 'called', 'chainDeferred', 'debug', 'errback', 'pause', 'paused', 'setTimeout', 'timeoutCall', 'unpause']
>>> dir(protocol.ClientFactory)
['__doc__', '__implemented__', '__module__', '__providedBy__', '__provides__', 'buildProtocol', 'clientConnectionFailed', 'clientConnectionLost', 'doStart', 'doStop', 'noisy', 'numPorts', 'protocol', 'startFactory', 'startedConnecting', 'stopFactory']

　　Twisted 官方称，“Twisted is event-based, asynchronous framework ”。这个“异步”功能的代表就是 defferred。
　　defferred 的作用类似于“多线程”，负责保障多头连接、多项任务的异步执行。
　　当然，defferred “异步”功能的实现，与多线程完全不同，具有以下特点：
　　１、defferred 产生的 event，是函数调用返回的对象；
　　２、defferred 代表一个连接任务，负责报告任务执行的延迟情况和最终结果；
　　３、对defferred 的操作，通过预定的“事件响应器”（event handler）进行。
　　有了defferred，即可对任务的执行进行管理控制。防止程序的运行，由于等待某项任务的完成而陷入阻塞停滞，提高整体运行的效率。 
'''
from twisted.internet import reactor, defer, protocol
class CallbackAndDisconnectProtocol(protocol.Protocol):     #协议
    # Twisted建立网络连接的固定套路 
    def connectionMade(self):
        self.factory.deferred.callback("Connected!")    # “事件响应器”handleSuccess对此事件作出处理 
        self.transport.loseConnection( )
class ConnectionTestFactory(protocol.ClientFactory):        #工厂
    # Twisted建立网络连接的固定套路 
    protocol = CallbackAndDisconnectProtocol
    def __init__(self):
        self.deferred = defer.Deferred( )　　　　# 报告发生了延迟事件，防止程序阻塞在这个任务上 
    def clientConnectionFailed(self, connector, reason):
        self.deferred.errback(reason)　　　　# “事件响应器”handleFailure对此事件作出处理 
def testConnect(host, port):
    testFactory = ConnectionTestFactory( )
    reactor.connectTCP(host, port, testFactory)
    return testFactory.deferred　　# 返回连接任务的deferred 
def handleSuccess(result, port):
    # deferred“事件响应器”：连接任务完成的处理 
    print "Connected to port %i" % port
    reactor.stop( )
def handleFailure(failure, port):
    # deferred“事件响应器”：连接任务失败的处理 
    print "Error connecting to port %i: %s" % (
        port, failure.getErrorMessage( ))
    reactor.stop( )
if __name__ == "__main__":
    import sys
    if not len(sys.argv) == 3:
        print "Usage: connectiontest.py host port"
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    connecting = testConnect(host, port)    # 调用函数，返回deferred 
    connecting.addCallback(handleSuccess, port)　　# 建立deferred“事件响应器” 
    connecting.addErrback(handleFailure, port)　　# 建立deferred“事件响应器” 
    reactor.run( )
