#coding=utf-8
import csv,random
"""
    高飞    于2009年5月12日
"""
def getDict():
    myfile=open('xingzuocesuan.db','r')
    reader=csv.reader(myfile)
    global dictCase
    dictCase={}
    for row in reader:      #文件中的每一行
        listCase=[]
        count=0
        #print row
        for item in row:        #每一行的各个元素
            #print count, item
            listCase.append(item)
            count=count+1
        dictCase[listCase[0]]=listCase[1]
#    for k,v in dictCase.items():
#        print k,v
    myfile.close()
    
def getXingzuo():
    global dictXingzuo
    dictXingzuo={1:'白羊座',2:'金牛座',3:'双子座',4:'巨蟹座',5:'狮子座',6:'处女座',7:'天秤座',8:'天蝎座',9:'射手座',10:'摩羯座',11:'水瓶座',12:'双鱼座',}
    i=random.randrange(1,13,1)
    global xingzuo
    xingzuo=dictXingzuo[i]
    print '系统随机生成的星座：%s\n'%(xingzuo)
    
    #xingzuo=raw_input('请输入您的星座')
    return xingzuo
    pass

def getResult(xingzuo):
    line=0
    print dictCase[xingzuo]
        
getDict()
getXingzuo()
getResult(xingzuo)