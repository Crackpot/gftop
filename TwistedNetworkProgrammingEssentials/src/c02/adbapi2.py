#!/usr/bin/env python
#coding=utf-8
from twisted.internet import reactor
from twisted.enterprise import adbapi
import pyPgSQL.PgSQL as PgSQL
dbpool=adbapi.ConnectionPool("pyPgSQL.PgSQL",
    user="crackpot",
    password="15263748",
    host="127.0.0.1",
    database="test"
)
def getData():
    return dbpool.runQuery("select user_id,name,age from users")
def printResult(l):
    for item in l:
        print item
getData().addCallback(printResult)
reactor.callLater(1,reactor.stop)
reactor.run()