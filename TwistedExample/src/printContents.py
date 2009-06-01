from twisted.web.client import getPage

from twisted.internet import reactor

def printContents(contents):
    '''
    This is the 'callback' function, added to the Deferred and called by
    it when the promised data is available
    '''

    print "The Deferred has called printContents with the following contents:"
    print contents

    # Stop the Twisted event handling system -- this is usually handled
    # in higher level ways
    reactor.stop()

# call getPage, which returns immediately with a Deferred, promising to
# pass the page contents onto our callbacks when the contents are available
deferred = getPage('http://baidu.com')

# add a callback to the deferred -- request that it run printContents when
# the page content has been downloaded
deferred.addCallback(printContents)

# Begin the Twisted event handling system to manage the process -- again this
# isn't the usual way to do this
reactor.run()
