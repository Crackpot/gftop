#coding=utf-8
import csv,random
"""
    高飞    于2009年5月11日
"""
def getDict():
    myfile=open('xuexingdapeiaiqing.db','r')
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
        dictCase[listCase[3]]=listCase
    #print dictCase
#    #解析列表
#    for item in listCase:
#        print item
    #解析字典
    for k,v in dictCase.items():
        title=k
        #print k,v
        for item in v:
            #print item   
            pass
    return dictCase
    myfile.close()

def getXuexing():
    #随机产生血型
    dictXuexing={'1':'A','2':'AB','3':'B','4':'O',}
    i=random.randrange(1,5,1)
    j=random.randrange(1,5,1)
    global xuexing1,xuexing2
    xuexing1=dictXuexing[str(i)]
    xuexing2=dictXuexing[str(j)]
    return xuexing1,xuexing2
    
def getResult(xuexing1,xuexing2):
    print '系统随机生成的血型分别是：%s,%s\n配对结果为:'%(xuexing1,xuexing2)
    #O型：O型
    #print dictCase[xuexing1+'型'+'：'+xuexing2+'型']
    count=0
    for item in dictCase[xuexing1+'型'+'：'+xuexing2+'型']:
        if count>3:     #前三行无用的数据不显示
            print item
        count=count+1
getDict()
getXuexing()
getResult(xuexing1, xuexing2)