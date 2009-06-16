#coding=utf-8
import psycopg2
# 创建连接……
cxn=psycopg2.connect(host='localhost',
    user='crackpot',
    password='15263748',
    database='test',    
)
# ……阻塞一段未知长短的时间

# 创建一个游标
cur=cxn.cursor()

# 做一次查询……
cur.execute('SELECT * FROM users')
# ……这能花很长的时间，或许甚至数分钟。

rows=cur.fetchall()
for item in rows:
    print item

cur.close()
cxn.commit()
cxn.close()