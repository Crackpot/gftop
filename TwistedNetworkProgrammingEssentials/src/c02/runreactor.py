#Example 2-1. runreactor.py
from twisted.internet import reactor
print "Running the reactor..."
reactor.run( )
print "Reactor stopped."
'''
>>> dir(reactor)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__implemented__', '__init__', '__module__', '__name__', '__new__', '__providedBy__', '__provides__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cancelCallLater', '_cancellations','_checkProcessArgs', '_disconnectSelectable', '_doReadOrWrite', '_eventTriggers', '_handleSigchld', '_handleSignals', '_initThreadPool', '_initThreads', '_insertNewDelayedCalls', '_lock', '_moveCallLaterSooner', '_newTimedCalls', '_pendingTimedCalls', '_preenDescriptors', '_reads', '_removeAll', '_stopThreadPool', '_writes', 'addReader', 'addSystemEventTrigger', 'addWriter', 'callFromThread', 'callInThread', 'callLater', 'callWhenRunning', 'cancelCallLater', 'connectSSL', 'connectTCP', 'connectUDP', 'connectUNIX', 'connectUNIXDatagram', 'connectWith', 'crash', 'disconnectAll', 'doIteration', 'doSelect', 'fireSystemEvent', 'getDelayedCalls', 'getReaders', 'getWriters', 'installResolver', 'installWaker','installed', 'iterate', 'listenMulticast', 'listenSSL', 'listenTCP', 'listenUDP', 'listenUNIX', 'listenUNIXDatagram', 'listenWith', 'mainLoop', 'removeAll', 'removeReader', 'removeSystemEventTrigger', 'removeWriter', 'resolve', 'resolver', 'run', 'runUntilCurrent', 'running', 'seconds', 'sigBreak', 'sigInt', 'sigTerm', 'spawnProcess', 'startRunning', 'stop', 'suggestThreadPoolSize', 'threadCallQueue', 'threadpool', 'threadpoolShutdownID', 'timeout', 'usingThreads', 'wakeUp', 'waker']
'''
