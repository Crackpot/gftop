#coding=utf-8
import csv,bsddb
dbName='/home/crackpot/workspace/mySuanming/src/hanzibihuaBsddb.db'

def convertDb():
    hanzibihuaBsddb=bsddb.btopen(dbName,'w')
    myfile=open('hanzibihua.db')
    reader=csv.reader(myfile)
    for row in reader:      #文件中的每一行
        #print row
        count=0
        listCase=[]
        for item in row:        #每一行的各个元素
            #print '内容为：%s,长度为%d'%(item,len(item))
            uniItem=unicode(item)
            listCase.append(uniItem)
            #print '内容为：%s,长度为%d'%(uniItem,len(uniItem))
            for i in range(len(uniItem)):
                #print uniItem[i]
                if ord(uniItem[i])>127:     #只留下中文汉字，数字除去
                    print uniItem[i],listCase[0]        #汉字，对应笔画数
                    hanzibihuaBsddb[uniItem[i].encode('utf-8')]=listCase[0]
                    pass
            count+=1
    hanzibihuaBsddb.sync()
    hanzibihuaBsddb.close()
    myfile.close()

def checkDb():
    for k,v in hanzibihuaBsddb.iteritems():
        print k,v
    pass

def getBihuashu():
    hanzibihuaBsddb=bsddb.btopen(dbName,'r')
    name='我是高飞'
    #print name,len(name)
    uniName=unicode(name)
    #print uniName,len(uniName)
    listBihua=[]
    for i in range(len(uniName)):
        #print uniName[i],uniName[i].encode('utf-8')
        listBihua.append(hanzibihuaBsddb[uniName[i].encode('utf-8')])
        #print listBihua[i]
    sumBihua=0
    for i in range(len(listBihua)):
        #print listBihua[i]
        sumBihua+=int(listBihua[i]) 
    print '您输入的姓名为：%s,字数为：%d，笔画总数为：%d'%(uniName,len(uniName),sumBihua)

#convertDb()
#checkDb()
getBihuashu()