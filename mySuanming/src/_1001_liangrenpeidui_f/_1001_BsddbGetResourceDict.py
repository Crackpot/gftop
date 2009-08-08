#coding=utf-8
import bsddb,os,csv
dbName='/home/crackpot/workspace/mySuanming/src/suanmingBsddb.db'

#suanmingBsddb=bsddb.btopen(dbName)
#suanmingBsddb=bsddb.btopen(dbName,'r')
suanmingBsddb=bsddb.btopen(dbName,'w')
myfile=open('liangrenpeidui.db')
reader=csv.reader(myfile)
for row in reader:      #文件的每一行
    #print row
    count=0
    listCase=[]
    for item in row:        #每一行的各个元素
        #print count, item
        listCase.append(item)
        count=count+1
#    print listCase[4][:listCase[4].find('：')],listCase[4][listCase[4].find('：')+3:]
#    print listCase[5][:listCase[5].find('：')],listCase[5][listCase[5].find('：')+3:]
#    print listCase[6][:listCase[6].find('：')],listCase[6][listCase[6].find('：')+3:]
#    print listCase[7][:listCase[7].find('：')],listCase[7][listCase[7].find('：')+3:]

    suanmingBsddb['1001_'+listCase[4][:listCase[4].find('：')]]=listCase[4][listCase[4].find('：')+3:]
    suanmingBsddb['1001_'+listCase[5][:listCase[5].find('：')]]=listCase[5][listCase[5].find('：')+3:]
    suanmingBsddb['1001_'+listCase[6][:listCase[6].find('：')]]=listCase[6][listCase[6].find('：')+3:]
    suanmingBsddb['1001_'+listCase[7][:listCase[7].find('：')]]=listCase[7][listCase[7].find('：')+3:]

    #suanmingBsddb['%s'%bsddbKey] = '%s'% listCase[1]
myfile.close()

#遍历数据库文件
for k,v in suanmingBsddb.iteritems():
    if k[:k.find('_')]=='1001':
        print k,v
#suanmingBsddb.sync()
suanmingBsddb.close()
