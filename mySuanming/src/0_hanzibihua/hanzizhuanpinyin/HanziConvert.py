#!/usr/bin/env python
# coding: utf8
import string
from pysqlite2 import dbapi2 as sqlite
from sys import argv

def getPinyin(text):
    pinyinlist=[]
    for i in range(len(text)):
        __Hanzicur.execute("select pinyin from hanzi where hanzi=?",(text[i]))
        pinyinlist.append([])
        for pinyin in __Hanzicur:
            pinyinlist[i].append(pinyin[0]+' ')
    poslist=[-1]*len(text)
    i=0
    results=[]
    n=0
    while (i>=0):
        poslist[i]=poslist[i]+1
        if (poslist[i]>=len(pinyinlist[i])) :
            poslist[i]=-1
            i=i-1
            continue
        if i==len(text)-1:
            results.append('')
            for t in range(len(text)):
                results[n]=results[n]+pinyinlist[t][poslist[t]]
            n=n+1
        else :
            i=i+1
    return results 
    
__HanziDBCon=sqlite.connect("hanzidb.db")
__Hanzicur=__HanziDBCon.cursor()
if __name__ == "__main__":
    if len(argv)<2 :
        print "Usage: python HanziConvert.py 汉字"
    else:
        for pinyin in getPinyin(unicode(argv[1],'utf8')):
            print pinyin