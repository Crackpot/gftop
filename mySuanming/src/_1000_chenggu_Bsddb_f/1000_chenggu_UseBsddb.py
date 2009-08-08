#coding=utf-8
"""
    高飞    于2009年5月16日
"""
import bsddb
suanmingBsddbName='/home/workspace/suanming/bsddb/suanmingBsddb.db'

def checkDb():
    suanmingBsddb=bsddb.btopen(suanmingBsddbName,'r')
    for k,v in suanmingBsddb.iteritems():
        if k[:k.find('_')]=='1000':
            print '%s==>%s'%(k,v)     
    suanmingBsddb.close()

def getScores():
    suanmingBsddb=bsddb.btopen(suanmingBsddbName,'r')
    global scoreSum
    #year=raw_input('年份')    #1900……2019
    year='1990'
    #month=raw_input('月份')    #一、二……腊
    month='六'
    #day=raw_input('日')    #初一、初二、三十    农历没有三十一
    day='十四'
    #hour=raw_input('时')    #0、1……23
    hour='4'
    Year='1000_Y'+year
    Month='1000_M'+month
    Day='1000_D'+day
    Hour='1000_H'+hour
    scoreY=float(suanmingBsddb[Year])
    scoreM=float(suanmingBsddb[Month])
    scoreD=float(suanmingBsddb[Day])
    scoreH=float(suanmingBsddb[Hour])
    scoreSum=scoreY+scoreM+scoreD+scoreH
    print scoreSum
    return scoreSum
    suanmingBsddb.close()

def getResult(score):
    suanmingBsddb=bsddb.btopen(suanmingBsddbName,'r')
    key='1000_'+str(int(score*10))
    try:
        print '解析：',suanmingBsddb[key]
    except Exception,e:
        #print e,key
        print '对不起，系统中没有与您姓名相对应的五行类型'
    
#checkDb()
getScores()
getResult(scoreSum)