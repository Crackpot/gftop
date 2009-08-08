#coding=utf-8
import csv,random
"""
    高飞    于2009年5月13日
"""

def getFenlei():
    myfile=open('zhougongjiemeng.db','r')
    reader=csv.reader(myfile)
    global dictCase
    dictCase={}
    global dictType1
    dictType1={}
    global dictType2
    dictType2={}
    for row in reader:      #文件的每一行
        #print row
        listCase=[]
        count=0
        for item in row:        #每一行的各个元素
            #print count, item
            listCase.append(item)
            count=count+1
        dictType1[listCase[0]]=listCase[0]
        dictType2[listCase[1]]=listCase[1]
        dictCase[listCase[0]+' '+listCase[1]]=listCase[2]
    #print listCase[0]+listCase[1]
    for k,v in dictType1.items():
        print k,v
#    for k,v in dictType2.items():
#        print k
#    for k,v in dictCase.items():
#        print k#,v
    #print len(dictCase)
    myfile.close()
    
getFenlei()