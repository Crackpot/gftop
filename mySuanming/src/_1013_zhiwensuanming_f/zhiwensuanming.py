#coding=utf-8
import csv,random
"""
    高飞    于2009年5月12日
"""
def getDict():
    myfile=open('zhiwensuanming.db','r')
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
        dictCase[listCase[1]]=listCase[2]
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

def getZhiwen():
    #随机产生血型
    dictZhiwen={'1':"xxxxx",'2':"xxxxo",'3':"xxxox",'4':"xxxoo",'5':"xxoxx",'6':"xxoxo",'7':"xxoox",'8':"xxooo",'9':"xoxxx",'10':"xoxxo",'11':"xoxox",'12':"xoxoo",'13':"xooxx",'14':"xooxo",'15':"xooox",'16':"xoooo",'17':"oxxxx",'18':"oxxxo",'19':"oxxox",'20':"oxxoo",'21':"oxoxx",'22':"oxoxo",'23':"oxoox",'24':"oxooo",'25':"ooxxx",'26':"ooxxo",'27':"ooxox",'28':"ooxoo",'29':"oooxx",'30':"oooxo",'31':"oooox",'32':"ooooo",}
    i=random.randrange(1,33,1)
    global Zhiwen
    #Zhiwen=raw_input('男左手，女右手。从拇指开始，斗（或叫箩）用O(OPQ的O,不是零0），簸箕用X（XYZ的X）代表。输入5个指纹代码(用小写字母)')
    Zhiwen=dictZhiwen[str(i)]
    return Zhiwen
    
def getResult(Zhiwen):
    print '系统随机生成的指纹类型是：%s\n其特点为：'%Zhiwen
    print dictCase[Zhiwen]
    
getDict()
getZhiwen()
getResult(Zhiwen)