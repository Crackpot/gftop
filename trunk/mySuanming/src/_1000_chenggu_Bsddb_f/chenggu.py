#coding=utf-8
import csv,random
"""
    高飞    于2009年5月12日
    只能用于农历生日的测算
    暂时找不到合适的阳历转阴历的程序，所以所用的时间均统一为阴历
    年月日时的分数单位为两，而结果的单位为钱。要对其进行换算
"""
def getDicts():
    myfile=open('chenggu.db','r')       #此文件存放最后的结果
    reader=csv.reader(myfile)
    global dictFate
    dictFate={}
    for row in reader:      #文件中的每一行，将它存在字典中
        #print row
        listFate=[]
        count=0
        for item in row:        #每一行的没一个元素
            #print count,item
            listFate.append(item)
            count=count+1
        dictFate[listFate[0]]=listFate[1]
        #print listFate
#    for k,v in dictFate.items():
#        print k,v
    myfile.close()
    
    myfile1=open('chenggu1.db','r')     #此文件存放年份
    reader1=csv.reader(myfile1)
    global dictYear
    dictYear={}
    for row in reader1:
        listYear=[]
        count=0
        #print row
        for item in row:
            #print count,item
            listYear.append(item)
            count=count+1
        #print listYear
        dictYear[listYear[0]]=listYear[1]
    #print dictYear
    myfile1.close()
    
    myfile2=open('chenggu2.db','r')     #此文件存放月份
    reader2=csv.reader(myfile2)
    global dictMonth
    dictMonth={}
    for row in reader2:     #文件中的每一行
        count=0
        #print row
        listMonth=[]
        for item in row:        #每一行的每个元素
            #print count,item
            listMonth.append(item)
            count=count+1
        #print listMonth
        dictMonth[listMonth[0]]=listMonth[1] 
    #print dictMonth
#    for k,v in dictMonth.items():
#        print k,v
    myfile2.close()
    
    myfile3=open('chenggu3.db','r')     #此文件存放天
    reader3=csv.reader(myfile3)
    global dictDay
    dictDay={}
    for row in reader3:         #文件中的没行
        #print row
        count=0
        listDay=[]
        for item in row:        #每一行的各个元素
            #print count, item
            listDay.append(item)
            #print listDay
            count=count+1
        dictDay[listDay[0]]=listDay[1]
    #print dictDay
#    for k,v in dictDay.items():
#        print k,v
    myfile3.close()
    
    myfile4=open('chenggu4.db','r')         #此文件存放时间
    reader4=csv.reader(myfile4)
    global dictTime
    dictTime={}
    for row in reader4:         #文件中的每一行
        listTime=[]
        count=0
        #print row       
        for item in row:        #每一行的各个元素
            #print count, item
            listTime.append(item)
            count=count+1
        #print listTime
        dictTime[listTime[0]]=listTime[1]
    #print dictTime
#    for k,v in dictTime.items():
#        print k,v
    myfile4.close()
    
    
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


 
def getInfo():
    """
        年、月、日、时
    """
    global year,month,day,time
    year=random.randrange(1900,2020,1)      #从1900年到2019年
    month=random.randrange(1,13,1)      #每年都有12个月
    global dictDayLunar
    dictDayLunar={1:"初一",2:"初二",3:"初三",4:"初四",5:"初五",6:"初六",7:"初七",8:"初八",9:"初九",10:"初十",11:"十一",12:"十二",13:"十三",14:"十四",15:"十五",16:"十六",17:"十七",18:"十八",19:"十九",20:"二十",21:"廿一",22:"廿二",23:"廿三",24:"廿四",25:"廿五",26:"廿六",27:"廿七",28:"廿八",29:"廿九",30:"三十",}
    global dictMonthLunar
    dictMonthLunar={1:"正",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十",11:"十一",12:"腊",}
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):    #这些月有31天
        day=random.randrange(1,31,1)        #农历没有三十一
    elif month==2:      #二月份要判断是否闰年来得到天数
        if isLeapYear(year):        #闰年29天
            day=random.randrange(1,30,1)
        else:       #平年28天
            day=random.randrange(1,29,1)
    else:       #4,6,9,11月份都是30天
        day=random.randrange(1,31,1)
    time=random.randrange(0,24,1)
    month=dictMonthLunar[month]
    day=dictDayLunar[day]       #因为要考察的是农历日期，将它变换成农历
#    year=raw_input('请输入您的出生年份')
#    month=raw_input('请输入您的出生月份')
#    day=raw_input('请输入您的出生日期')
#    time=raw_input('请输入您的出生时间')
    print '系统随机生成的时间为：%d年 %s月 %s %d时'%(year,month,day,time)
    return year,month,day,time
    pass

def getResult(year,month,day,time):
    print '%d年 %s月 %s %d时'%(year,month,day,time)
    #print type(day)
    scoreYear=float(dictYear[str(year)])
    #print type(month)
    scoreMonth=float(dictMonth[month])
    #print type(scoreMonth),scoreMonth
    #print type(month)
    #print day
    scoreDay=float(dictDay[day])
    scoreTime=float(dictTime[str(time)])
    #print type(scoreTime),scoreTime
    score=int((scoreYear+scoreMonth+scoreDay+scoreTime)*10)     #转换单位    年月日时的分数单位为两，而结果的单位为钱
    print '您的骨重为：%d两%d钱'%(int(score/10),score%10)
    result=dictFate[str(score)]
    print result
    pass


getDicts()
getInfo()
getResult(year, month, day, time)
