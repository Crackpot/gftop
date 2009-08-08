#!/usr/bin/env python
# coding: utf8
import string
import re
from pysqlite2 import dbapi2 as sqlite

def parseline(line):
    (key,hanzis)=string.split(line,'=>');
    key=key.strip()
    hanzilist=unicode(hanzis.strip(),'utf8')
    hanzilist=re.sub("\\\\\\\'",'',hanzilist)
    hanzilist=re.sub(",",'',hanzilist)
    for char in hanzilist:
        cur.execute("insert into hanzi(hanzi,pinyin) values (?,?)", (char,key))
 
if __name__ == "__main__":
    con = sqlite.connect("hanzidb.db")
    cur=con.cursor()
    cur.execute("delete from hanzi")
    file=open("hanzi.txt","r")
    for line in file.readlines():
        parseline(line)
    con.commit()
