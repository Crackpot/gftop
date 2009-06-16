#!/usr/bin/env python
#coding=utf-8
'''
>>> dir(adbapi)
['Connection', 'ConnectionLost', 'ConnectionPool', 'Transaction', 'Version', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '_safe', '_unreleasedDeprecation', '_unreleasedVersion', 'deprecated', 'log', 'reflect', 'safe', 'sys', 'threads']
'''
from twisted.internet import reactor
from twisted.enterprise import adbapi
import psycopg2
dbpool=adbapi.ConnectionPool("psycopg2",
    host="localhost",
    user="crackpot",
    password="15263748",
    database="test",
)
# 等同于cursor.execute(statement)，返回cursor.fetchall()：
def _getData(txn,user):
    # 这将在一个线程中跑，所以我们可以使用阻塞方式的调用
    txn.execute('SELECT * FROM users')
    # ……把txn当作游标来用吧……
    result=txn.fetchall()
    if result:
        return result
    else:
        return None
def getData(user):
    return dbpool.runInteraction(_getData,user)
def printResult(data):
    if data!=None:
        print "数据：\n", data
    else:
        print "没有符合条件的数据"
getData("crackpot").addCallback(printResult)
reactor.callLater(1,reactor.stop)
reactor.run()