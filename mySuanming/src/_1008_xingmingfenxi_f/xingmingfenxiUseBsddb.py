#coding=utf-8
"""
    高飞    于2009年5月16日
    更新到svn目录之后请更改数据库名称，否则将无法使用
"""
import csv,bsddb
hanzibihuaBsddbName='/home/crackpot/workspace/mySuanming/src/hanzibihuaBsddb.db'
suanmingBsddbName='/home/crackpot/workspace/mySuanming/src/suanmingBsddb.db'

def checkDb():
#    hanzibihuaBsddb=bsddb.btopen(hanzibihuaBsddbName,'r')
#    for k,v in hanzibihuaBsddb.iteritems():
#        print k,v
#    pass
#    hanzibihuaBsddb.close()

    suanmingBsddb=bsddb.btopen(suanmingBsddbName,'r')
    for k,v in suanmingBsddb.iteritems():
        if k[:k.find('_')]=='1008':
            print '%s==>%s'%(k,v)     
    suanmingBsddb.close()

def getBihuashu():
    name='诸葛亮'
    global sumBihua
    sumBihua=0
    hanzibihuaBsddb=bsddb.btopen(hanzibihuaBsddbName,'r')
    #print name,len(name)
    uniName=unicode(name)
    #print uniName,len(uniName)
    zishu=len(uniName)      #姓名中有几个字数
    listBihua=[]
    for i in range(len(uniName)):
        bihuashu=hanzibihuaBsddb[uniName[i].encode('utf-8')]
        listBihua.append(bihuashu)       #将汉字在数据库中查询并返回它的笔画数
        #print '%s,%d'%(uniName[i],int(listBihua[i]))#,uniName[i].encode('utf-8'))
    for i in range(len(listBihua)):
        #print listBihua[i]
        sumBihua+=int(listBihua[i])
    print '您输入的姓名为：%s，笔画总数为：%d'%(uniName,sumBihua)
    return sumBihua

def getResult(bihua):
    print '您的姓名解析为：'
    suanmingBsddb=bsddb.btopen(suanmingBsddbName,'r')
    key='1008_'+str(bihua)
    try:
        print suanmingBsddb[key]
    except Exception,e:
        #print e,key
        print '对不起，系统中没有与您姓名相对应的解析'
    suanmingBsddb.close()

#checkDb()        
getBihuashu()
getResult(sumBihua)