#!/usr/bin/env python
#coding=utf-8

import os
from random import randrange as rrange
COLSIZ=10
RDBMSs={
    'p':'pyPgSQL',
}
DB_EXC=None

def setup():
    return RDBMSs[raw_input('''
Choose a database system:
(M)ySQL
(G)adfly
(S)QLite
(P)Postgres
    ''').strip().lower()[0]]
def connect(db,dbName):
    global DB_EXC
    dbDir='%s_%s'%(db,dbName)
    if db=='pyPgSQL':
        try:
            import pyPgSQL.PgSQL as PgSQL
        except ImportError,e:
            print e
        try:
            cxn=PgSQL.connect(host='localhost',
                database='test',
                user='crackpot',
                password='15263748',
            )
            cur=cxn.cursor()
        except Exception,e:
            print e
        try:
            cur.execute('SELECT * FROM users')
            rows=cur.fetchall()
            for i in rows:
                print i
        except Exception,e:
            print e
def main():
    db=setup()
    cxn=connect(db,'test')
if __name__=='__main__':
    main()