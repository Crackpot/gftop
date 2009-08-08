#coding=utf-8
import bsddb,os,csv
dbName='/home/crackpot/workspace/mySuanming/src/suanmingBsddb.db'

#suanmingBsddb=bsddb.btopen(dbName)
#suanmingBsddb=bsddb.btopen(dbName,'r')
suanmingBsddb=bsddb.btopen(dbName,'w')
myfile=open('xuexingdapeiaiqing.db')
reader=csv.reader(myfile)
for row in reader:      #文件的每一行
    #print row
    count=0
    listCase=[]
    for item in row:        #每一行的各个元素
        #print count, item
        listCase.append(item)
        count=count+1
    print '%s==>%s'%('1010_'+listCase[4][:listCase[4].find('：')],listCase[4][listCase[4].find('：'):]+'\n'+listCase[5])

    suanmingBsddb['1010_'+listCase[4][:listCase[4].find('：')]] = '%s'%listCase[4][listCase[4].find('：'):]+'\n'+listCase[5]
myfile.close()


#遍历数据库文件
for k,v in suanmingBsddb.iteritems():
    if k[:k.find('_')]=='1010':
        print k,v
#suanmingBsddb.sync()