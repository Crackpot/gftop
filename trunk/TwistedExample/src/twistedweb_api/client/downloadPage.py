#coding=utf-8
'''
     def downloadPage(url, file, *args, contextFactory=None, **kwargs):  (source)
        Download a web page to a file.
            Parameters    file    path to file on filesystem, or file-like object.
                                 See HTTPDownloader to see what extra args can be passed. 
'''
from twisted.web.client import downloadPage
from twisted.internet import reactor
def stopReactor(contents):
    reactor.stop()
deferred=downloadPage('http://www.baidu.com','tmp.html')
deferred.addCallback(stopReactor)
reactor.run()