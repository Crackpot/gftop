#coding=utf-8
import csv,random
"""
    高飞    于2009年5月11日
"""
def getDict():
    myfile=open('xuexingjiexi.db','r')
    reader=csv.reader(myfile)
    global dictCase
    dictCase={}
    for row in reader:      #整个文件的每一行
        count=0     #标记没行的第几个元素
        #print row
        listCase=[]
        for item in row:        #没行的各个元素
            #print count,item
            count=count+1
            listCase.append(item)
        dictCase[listCase[0]]=listCase[1]
    #print dictCase
#        #解析列表
#        for item in listCase:
#            print item
    #解析字典
    for k,v in dictCase.items():
        #print k,v    
        pass
    return dictCase
    myfile.close()

def getXuexing():
    #随机产生血型
    dictXuexing={'1':'A','2':'AB','3':'B','4':'O',}
    i=random.randrange(1,5,1)
    global xuexing
    xuexing=dictXuexing[str(i)]
    return xuexing
    
def getResult(xuexing):
    print '系统随机生成的血型是：%s\n其特点为：'%xuexing
    print dictCase[xuexing]
    
getDict()
getXuexing()
getResult(xuexing)