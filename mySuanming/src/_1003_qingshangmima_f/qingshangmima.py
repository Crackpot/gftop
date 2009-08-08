#coding=utf-8
import csv,random
"""
    高飞    于2009年5月12日
"""
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
        dictCase[listCase[2]]=listCase
        #print listCase
    #print dictCase
    for k,v in dictCase.items():
        #print '\n键名：%s'%k
        for item in v:
            #print item
            pass
    #print 'dictCase的长度：%d'%len(dictCase)
    myfile.close()
    
def getXingzuo():
    global dictXingzuo
    dictXingzuo={1:'白羊座',2:'金牛座',3:'双子座',4:'巨蟹座',5:'狮子座',6:'处女座',7:'天秤座',8:'天蝎座',9:'射手座',10:'摩羯座',11:'水瓶座',12:'双鱼座',}
    i=random.randrange(1,13,1)
    j=random.randrange(1,13,1)
    global xingzuo1
    xingzuo1=dictXingzuo[i]
    global xingzuo2
    xingzuo2=dictXingzuo[j]
    print '系统随机生成的星座分别是：%s,%s\n'%(xingzuo1,xingzuo2)
    #xingzuo1=raw_input('请输入您的星座')
    #xingzuo2=raw_input('请输入对方的星座')
    return xingzuo1,xingzuo2
    pass

def getResult(xingzuo1,xingzuo2):
    line=0
    for item in dictCase[xingzuo1+'：'+xingzuo2]:
        if line>=2:
            print item
        line=line+1
        
getDict()
getXingzuo()
getResult(xingzuo1, xingzuo2)