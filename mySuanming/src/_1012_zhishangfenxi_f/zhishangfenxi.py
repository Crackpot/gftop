#coding=utf-8
import csv,random
"""
    高飞    于2009年5月12日
"""
def getDict():
    myfile=open('zhishangfenxi.db','r')
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
#        #解析列表
#        for item in listCase:
#            print item
    #print dictCase

    #解析字典
    for k,v in dictCase.items():
        #print '%s：\n%s\n'%(k,v)    
        pass
    return dictCase
    myfile.close()

def getXingzuo():
    #随机产生星座
    dictXingzuo={'1':"水瓶座",'2':"白羊座",'3':"金牛座",'4':"双子座",'5':"巨蟹座",'6':"狮子座",'7':"处女座",'8':"天秤座",'9':"天蝎座",'10':"射手座",'11':"摩羯座",'12':"双鱼座"}
    i=random.randrange(1,13,1)
    global xingzuo
    #xingzuo=raw_input('请输入您的星座：')
    #xingzuo='天蝎座'
    xingzuo=dictXingzuo[str(i)]
    return xingzuo
    
def getResult(xingzuo):
    print '系统随即生成的星座是：%s\n其智商分析为：'%xingzuo
    print dictCase[xingzuo]
    
getDict()
getXingzuo()
getResult(xingzuo)