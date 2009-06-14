#Example 2-2. calllater.py
from twisted.internet import reactor
import time
def printTime():
    print "Current time is",time.strftime("%H:%M:%S")
def stopReactor():
    print "Stopping reactor"
    reactor.stop()
'''
    callLater(self, _seconds, _f, *args, **kw) method of wisted.internet.selectreactor.SelectReactor instance
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