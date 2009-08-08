#coding=utf-8
import csv,random
"""
    高飞    于2009年5月12日
"""
def getDict():
    myfile=open('shuxiangfenxi.db','r')
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

def getShuxiang():
    #随机产生血型
    dictShuxiang={'1':'鼠','2':'牛','3':'虎','4':'兔','5':'龙','6':'蛇','7':'马','8':'羊','9':'猴','10':'鸡','11':'狗','12':'猪',}
    i=random.randrange(1,13,1)
    global shuxiang
    shuxiang=dictShuxiang[str(i)]
    #print shuxiang
    return shuxiang
    
def getResult(shuxiang):
    print '系统随机生成的属相是：%s\n分析如下：'%shuxiang
    print dictCase[shuxiang]
    
getDict()
getShuxiang()
getResult(shuxiang)