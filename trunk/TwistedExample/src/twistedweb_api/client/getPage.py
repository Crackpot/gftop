#coding=utf-8
"""
    def getPage(url, *args, contextFactory=None, **kwargs):  (source)
    Download a web page as a string.
    Download a page. Return a deferred, which will callback with a page (as a string) or errback with a description of the error.
    See HTTPClientFactory to see what extra args can be passed. 
"""
from twisted.web.client import getPage
from twisted.internet import reactor
def printContents(contents):
    '''
    This is the 'callback' function, added to the Deferred and called by
    it when the promised data is available
    '''
    print "The Deferred has called printContents with the following contents:"
    print contents
    # Stop the Twisted event handling system -- this is usually handled in higher level ways
    reactor.stop()
# call getPage, which returns immediately with a Deferred, promising to pass the page contents onto our callbacks when the contents are available
deferred = getPage('http://www.g.cn/')
'''
    ['__doc__', '__init__', '__module__', '__repr__', '__str__', '_continue', '_debugInfo', '_runCallbacks', '_runningCallbacks', '_startRunCallbacks', 'addBoth', 'addCallback', 'addCallbacks', 'addErrback', 'callback', 'callbacks', 'called', 'chainDeferred', 'debug', 'errback', 'pause', 'paused', 'setTimeout', 'timeoutCall', 'unpause']
'''
# add a callback to the deferred -- request that it run printContents when the page content has been downloaded
deferred.addCallback(printContents)
# Begin the Twisted event handling system to manage the process -- again this isn't the usual way to do this
reactor.run()