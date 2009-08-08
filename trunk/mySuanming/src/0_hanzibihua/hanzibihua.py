#coding=utf-8
import csv
#myfile=open('hanzibihua.db','r')
#reader=csv.reader(myfile)
#for row in reader:      #文件中的每一行
#    #print row
#    count=0
#    dictCase=[]
#    for item in row:        #每一行的各个元素
#        #print count,len(item), item
#        dictCase.append(item)
#        if '飞' in item:
#            for i in dictCase:
#                bihuashu=int(dictCase[0])
#        count+=1
#print '笔画数为：%d'%bihuashu
#myfile.close()
def getName():
    #strName=raw_input('请输入您的姓名：')
    strName='高飞'
#    原始情况
#    print strName,len(strName)
#    for i in range(len(strName)):
#        print strName[i]
    #将字符串转换为unicode形式
    strName=unicode(strName,'utf-8')
    print ('您的姓名为：%s；长度为：%d')%(strName,len(strName))
    for i in range(len(strName)):
        print strName[i]
    
    
    
    
getName()