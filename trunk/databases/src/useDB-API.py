#coding=utf-8

#1
import pyPgSQL.PgSQL as PgSQL
cxn=PgSQL.connect(host='localhost',
    database='test',
    user='crackpot',
    password='15263748'
)
'''
#2
import psycopg 
cxn=psycopg.connect(host='localhost',
    database='test',
    user='crackpot',
    password='15263748',
)
'''
'''
#3
from pyPgSQL import PgSQL
cxn=PgSQL.connect(host='localhost',
    database='test',
    user='crackpot',
    password='15263748',
)
'''

cur=cxn.cursor()
cur.execute('SELECT * FROM users')
rows=cur.fetchall()
for i in rows:
    print i
cur.close()
cxn.commit()
cxn.close()