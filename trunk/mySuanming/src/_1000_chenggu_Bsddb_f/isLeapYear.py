#coding=utf-8
def isLeapYear(year):
    year=year
    leap=0
    if year%4==0 and year%100!=0:
        leap=1
    if year%100==0 and year%400==0:
        leap=1
    if leap==1 :
        print '%d年是闰年！'%year
    else:
        print '%d年不是闰年！'%year
    return leap

if isLeapYear(2008):
    print '这年的二月份有29天'
    
    
    
    
    
    
