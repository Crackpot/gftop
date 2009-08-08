#coding=utf-8
import bsddb,os,csv
dbName='/home/crackpot/workspace/mySuanming/src/suanmingBsddb.db'

#suanmingBsddb=bsddb.btopen(dbName)
#suanmingBsddb=bsddb.btopen(dbName,'r')
suanmingBsddb=bsddb.btopen(dbName,'w')
myfile=open('shengrimima.db')
reader=csv.reader(myfile)
for row in reader:      #文件的每一行
    #print row
    count=0
    listCase=[]
    for item in row:        #每一行的各个元素
        #print count, item
        listCase.append(item)
        count=count+1
    #print '%s==>%s'%('1006_'+listCase[1],listCase[2])

    suanmingBsddb['%s'%'1006_'+listCase[1]] = '%s'% listCase[2]
myfile.close()


#遍历数据库文件
for k,v in suanmingBsddb.iteritems():
    if k[:k.find('_')]=='1006':
        print k,v
#suanmingBsddb.sync()
