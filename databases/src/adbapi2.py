#!/usr/bin/env python
#coding=utf-8
from twisted.internet import reactor
from twisted.enterprise import adbapi
import psycopg2
dbpool=adbapi.ConnectionPool("psycopg2",
    host="localhost",
    user="crackpot",
    password="15263748",
    database="test",
)

def getData():
    return dbpool.runQuery("select * from users")
def printResult(l):
    for item in l:
        print item
getData().addCallback(printResult)
reactor.callLater(1,reactor.stop)
reactor.run()