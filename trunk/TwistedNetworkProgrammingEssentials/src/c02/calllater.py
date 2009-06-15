#Example 2-2. calllater.py
#coding=utf-8
'''
>>> dir(reactor)
['__class__', '__delattr__', '__dict__', '__doc__', '__getattribute__', '__hash__', '__implemented__', '__init__', '__module__', '__name__', '__new__', '__providedBy__', '__provides__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__str__', '__weakref__', '_cancelCallLater', '_cancellations', '_checkMode', '_checkProcessArgs', '_disconnectSelectable', '_doReadOrWrite', '_eventTriggers', '_handleSigchld', '_handleSignals', '_initThreadPool', '_initThreads', '_insertNewDelayedCalls', '_installSignalHandlers', '_justStopped', '_lock', '_moveCallLaterSooner', '_newTimedCalls', '_pendingTimedCalls', '_preenDescriptors', '_reads', '_reallyStartRunning', '_removeAll', '_started', '_stopThreadPool', '_stopped', '_unspecified', '_writes', 'addReader', 'addSystemEventTrigger', 'addWriter', 'callFromThread', 'callInThread', 'callLater', 'callWhenRunning', 'cancelCallLater', 'connectSSL', 'connectTCP', 'connectUDP', 'connectUNIX', 'connectUNIXDatagram', 'connectWith', 'crash', 'disconnectAll', 'doIteration', 'doSelect', 'fireSystemEvent', 'getDelayedCalls', 'getReaders', 'getWriters', 'installResolver', 'installWaker', 'installed', 'iterate', 'listenMulticast', 'listenSSL', 'listenTCP', 'listenUDP', 'listenUNIX', 'listenUNIXDatagram', 'listenWith', 'mainLoop', 'removeAll', 'removeReader', 'removeSystemEventTrigger', 'removeWriter', 'resolve', 'resolver', 'run', 'runUntilCurrent', 'running', 'seconds', 'sigBreak', 'sigInt', 'sigTerm', 'spawnProcess', 'startRunning', 'stop', 'suggestThreadPoolSize', 'threadCallQueue', 'threadpool', 'threadpoolShutdownID', 'timeout', 'usingThreads', 'wakeUp', 'waker']
    twisted的套路概括成一句话，“一个中心，两个基本点”，现在就从这个“中心”聊起。
    Twisted 官方说，“ Twisted is an event-driven networking framework ”。事实的确如此。从其运行机制上看，event 是 Twisted 运转的引擎，是发生各种动作的启动器，是牵一发而动全身的核心部件。从其架构组成上看，它是紧密围绕event设计的；它的具体应用 application，主要是定义、实现各式各样的event，由此完成不同网络协议的连接和输入输出任务，满足用户的实际需求；从其 application的文本形式上，可以直接看到，它的应用程序，基本上由一系列event构成。
在 Twisted 应用中，reactor 的任务是为程序运行建立必须的全局循环（event loop），所起的作用，相当于 Python 应用中的 MainLoop()。
    reactor 的用法很简单，一般只用两个：reactor.run() 启动全局循环，reactor.stop() 停止全局循环（程序终止）。 
'''
from twisted.internet import reactor
import time
def printTime():
    print "Current time is",time.strftime("%H:%M:%S")
def stopReactor():
    print "Stopping reactor"
    reactor.stop()
'''
>>> help(reactor.callLater)
Help on method callLater in module twisted.internet.base:

callLater(self, _seconds, _f, *args, **kw) method of twisted.internet.selectreactor.SelectReactor instance
    See twisted.internet.interfaces.IReactorTime.callLater.
'''
reactor.callLater(1,printTime)
reactor.callLater(2,printTime)
reactor.callLater(3,printTime)
reactor.callLater(4,printTime)
reactor.callLater(5,stopReactor)
print "Running the reactor..."
reactor.run()
print "Reactor stopped"