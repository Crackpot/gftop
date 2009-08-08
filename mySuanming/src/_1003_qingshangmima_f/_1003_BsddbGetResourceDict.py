#coding=utf-8
import bsddb,os,csv
dbName='/home/crackpot/workspace/mySuanming/src/suanmingBsddb.db'

#suanmingBsddb=bsddb.btopen(dbName)
#suanmingBsddb=bsddb.btopen(dbName,'r')
suanmingBsddb=bsddb.btopen(dbName,'w')

def getDict():
    myfile=open('qingshangmima.db','r')
    reader=csv.reader(myfile)
    global dictCase
    dictCase={}
    for row in reader:      #文件中的每一行
        #print row
        count=0
        listCase=[]
        for item in row:        #每一行的各个元素
            #print count, item
            listCase.append(item)
            count=count+1
        #print '%s\n%s'%('1003_'+listCase[2],listCase[3]+'\n'+listCase[4])
        suanmingBsddb['1003_'+listCase[2]]=listCase[3]+'\n'+listCase[4]
        #dictCase[listCase[2]]=listCase
        #print listCase
#    #print dictCase
#    #解析字典
#    for k,v in dictCase.items():
#        #print '\n键名：%s'%k
#        for item in v:
#            #print item
#            pass
    #print 'dictCase的长度：%d'%len(dictCase)
    myfile.close()

getDict()

#遍历数据库文件
for k,v in suanmingBsddb.iteritems():
    if k[:k.find('_')]=='1003':
        print k,v
#suanmingBsddb.sync()
suanmingBsddb.close()