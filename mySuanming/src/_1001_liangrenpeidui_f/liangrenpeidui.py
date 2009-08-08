#coding=utf-8
import csv,random
"""
    高飞    于2009年5月11日
"""
def getDict():
    myfile=open('liangrenpeidui.db','r')
    reader=csv.reader(myfile)
    global dictCase
    dictCase={}
    for row in reader:
        count=0
        #print row        #无法显示中文
        #print type(row)     #row的类型是列表
        listCase=[]
        for item in row:        #列表中的每一项（每一行用逗号分开的引号中的内容）
            #print count,item
            listCase.append(item)
            count=count+1
        #print 'listCase[3]',listCase[3]        #如“listCase[3] 鼠：牛”
        #print 'len(row)',len(row)    #每个列表的长度为8
        dictCase[listCase[3]]=listCase
        #print 'listCase',listCase
    #print 'dictCase',dictCase
    #解析字典和列表
    for k,v in dictCase.items():
        peiduiqingkuang=k       #配对情况    如：“狗：兔”
        xiangjie=v      #详细讲解
        for item in xiangjie:
            #print item
            pass
    return dictCase
    myfile.close()

    
def getShengxiaoXingbie():
    global shengxiao1
    global shengxiao2
    global xingbie1
    global xingbie2
#    shengxiao1=raw_input('请输入您的生肖：')
#    shengxiao2=raw_input('请输入对方的生肖：')
#    xingbie1=raw_input('请输入您的性别：')
#    xingbie2=raw_input('请输入对方的性别：')
    #用字典的形式存储生肖和性别
    dictShengxiao={'1':'鼠','2':'牛','3':'虎','4':'兔','5':'龙','6':'蛇','7':'马','8':'羊','9':'猴','10':'鸡','11':'狗','12':'猪',}
    xingbieDict={'1':'男','2':'女'}
    #产生两个随机数以生成两个随机的生肖
    i=random.randrange(1,13,1)
    j=random.randrange(1,13,1)
    shengxiao1=dictShengxiao[str(i)]
    shengxiao2=dictShengxiao[str(j)]
    x=random.randrange(1,3)     #产生一个性别，使另外一个为异性
    if x==1:
        y=2
    else:
        y=1
    xingbie1=xingbieDict[str(x)]
    xingbie2=xingbieDict[str(y)]
    print '系统随机生成的两个属相分别为：%s,%s;两个性别分别为：%s,%s'%(shengxiao1,shengxiao2,xingbie1,xingbie2)
    return shengxiao1,shengxiao2,xingbie1,xingbie2

def getValue(shengxiao1,shengxiao2,xingbie1,xingbie2):
    for item in dictCase[shengxiao1+'：'+shengxiao2]:
        if (xingbie1+shengxiao1+'＋'+xingbie2+shengxiao2) in item:       #如“男龙＋女狗”
            print item
    
getDict()
getShengxiaoXingbie()
getValue(shengxiao1, shengxiao2, xingbie1, xingbie2)