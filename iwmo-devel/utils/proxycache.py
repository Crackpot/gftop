#coding=utf-8
import datetime,types
from twisted.internet import defer
#import settings
from twisted.python import logfile
from twisted.internet.address import IPv4Address
from twisted.internet import reactor
import iwproxypool as mp

serverAddress=IPv4Address('TCP', '127.0.0.1', 11000)
mp.installPool(serverAddress)
pcache=mp.defaultCachePool()

if __name__=='__main__':
    def c(result,phone):
        print phone,result
        #reactor.stop()
    phone='15979122400'
    pcache.gpa(phone).addCallback(c,phone)
    
    reactor.run()