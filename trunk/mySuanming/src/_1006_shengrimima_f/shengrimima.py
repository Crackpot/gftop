#coding=utf-8
import csv,random
"""
    高飞    于2009年5月12日
"""
def getDict():
    myfile=open('shengrimima.db','r')
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
#    #解析列表
#    for item in listCase:
#        print item
    #解析字典
    for k,v in dictCase.items():
        #print k,v    
        pass
    return dictCase
    myfile.close()

def isLeapYear(year):
    year=year
    leap=0
    if year%4==0 and year%100!=0:
        leap=1
    if year%100==0 and year%400==0:
        leap=1
#    if leap==1 :
#        print "%d年是闰年！"%year
#    else:
#        print "%d年不是闰年！"%year
    return leap

def getShengri():
    #随机产生属相
    global year
    year=random.randrange(1900,2020,1)
    #year=raw_input('请输入您的出生年份：')
    global month
    month=random.randrange(1,13,1)
    #month=raw_input('请输入您的出生月份：')
    global day
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):    #这些月有31天
        day=random.randrange(1,32,1)        #这些月份为31天
    elif month==2:      #二月份要判断是否闰年来得到天数
        if isLeapYear(year):        #闰年29天
            day=random.randrange(1,30,1)
        else:       #平年28天
            day=random.randrange(1,29,1)
    else:       #4,6,9,11月份都是30天
        day=random.randrange(1,31,1)
    #day=raw_input('请输入您的出生日期')
    return year,month,day

    
def getResult(year,month,day):
    print '系统随机产生的时间为%d年%d月%d日\n'%(year,month,day)
    strMonth=str(month)
    if day>9:
        strDay=str(day)
    else:
        strDay='0'+str(day)
    print dictCase[strMonth+strDay]
    
getDict()
getShengri()
getResult(year, month, day)