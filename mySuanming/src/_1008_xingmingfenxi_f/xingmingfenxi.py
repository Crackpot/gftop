#coding=utf-8
import csv,random
"""
    高飞    于2009年5月11日
"""
def getDict():
    myfile=open('xingmingfenxi.db','r')
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

def getBihuashu():
    #随机产生比划数
    global bihuashu
#    bihuashu=raw_input('请输入您姓名的比划数')
#    if bihuashu>162:
#        print '输入的比划数不能大于162！'
#        getBihuashu()
    bihuashu=random.randrange(1,162,1)
    if bihuashu>81:
        bihuashu=bihuashu-81
    return bihuashu
    
def getResult(bihuashu):
    print '随机生成的姓名比划数是：%d\n其特点为：'%bihuashu
    print dictCase[str(bihuashu)]
    
getDict()
getBihuashu()
getResult(bihuashu)