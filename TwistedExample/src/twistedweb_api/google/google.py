#coding=utf-8
from twisted.web.google import checkGoogle
from twisted.internet import reactor
string='python twisted'

def reactorStop(contents):
    print contents
    reactor.stop()
deferred=checkGoogle(string)
deferred.addCallback(reactorStop)
reactor.run()