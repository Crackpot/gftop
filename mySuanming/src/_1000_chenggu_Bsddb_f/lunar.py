#!/usr/bin/env                                         
#coding=utf-8                                                           
'''''                                                                              
 Usage:  ccal Month [4-Digit-Year]                                                
    or:  ccal 4-Digit-Year Month                                                  
                                                                                  
 This Python script is to show Solar and Lunar calender at the                    
 same time. You need to have Python (2.0 or above) installed.                     
                                                                                  
 Acceptable date range:  1900/2 -- 2049/12                                        
                                                                                  
 Output contains Chinese characters (mainland GB2312 encoding),                   
 must be viewed in a Chinese-enabled system or "cxterm" etc.                      
 programms under UNIX X-Windows.                                                  
                                                                                  
 The major reference for me to compose this program is:                           
 lunar-2.1.tgz (1992), composed by                                                
     Fung F. Lee <[email]lee@umunhum.stanford.edu[/email]> and                                   
     Ricky Yeung  <[email]Ricky.Yeung@Eng.Sun.Com[/email]> .                                     
                                                                                  
 And Lee and Yeung refered to:                                                    
     1. "Zhong1guo2 yin1yang2 ri4yue4 dui4zhao4 wan4nian2li4"                     
         by Lin2 Qi3yuan2. 《中国阴阳日月对照万年历》．林                         
     2. "Ming4li3 ge2xin1 zi3ping2 cui4yan2" by Xu2 Le4wu2.                       
         《命理革新子平粹言》．徐                                                 
     3.  Da1zhong4 wan4nian2li4. 《大众万年历》                                   
                                                                                  
 License:                                                                         
     GNU General Public License (GPL, see [url]http://www.gnu.org[/url]).                    
     In short, users are free to use and distribute this program                  
     in whole. If users make revisions and distribute the revised                 
     one, they are required to keep the revised source accessible                 
     to the public.                                                               
                                                                                  
 Version:                                                                         
     0.2.0,  Jan/6/2002, ShengXiao(生肖), lunar leap month(闰月)                  
             added.                                                               
     0.1.0,  Jan/4/2002                                                           
                                                                                  
         --- Changsen Xu <[email]xucs007@yahoo.com[/email]>                                      
'''                                                                               
                                                                                   
#remember, in this program:                                                       
#   month=0 means Januaray, month=1 means February ...;                           
#   day=0 means the first day of a month, day=1 means the second day,             
#       so as to easy to manipulate Python lists.                                 
#   year=0 is 1900, until the last step to output                                 
                                                                                   
daysInSolarMonth= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]                
lunarMonthDays  = [29,30] # a short (long) lunar month has 29 (30) days */        
                                                                                   
shengXiaoEn     = ["Mouse", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",           
                    "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]            
shengXiaoGB     = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡",    
                    "狗", "猪"]                                                    
zhiGB           = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉",    
                    "戌", "亥"]                                                    
ganGB           = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]    
                                                                                   
monthEn         = ['January', 'February', 'March', 'April', 'May', 'June',        
                    'July', 'August', 'September', 'October', 'November',          
                    'December']                                                    
weekdayEn       = ["Monday", "Tuesday", "Wednesday", "Thursday",                  
                    "Friday", "Saturday", "Sunday"]                                
weekdayGB       = ["一", "二", "三", "四", "五", "六", "日"]                      
numGB           = ['○', "一", "二", "三", "四", "五", "六", "七", "八", "九","十"]                                                          
lunarHoliday    = {'0_0':'春节', '4_4':'端午', '7_14':'中秋', '8_8':'重阳',       
                    '0_14':'元宵'}                                                 
                                                                                   
                                                                                   
#   encoding:                                                                     
#               b bbbbbbbbbbbb bbbb                                               
#      bit#     1 111111000000 0000                                               
#               6 543210987654 3210                                               
#               . ............ ....                                               
#      month#     000000000111                                                    
#               M 123456789012   L                                                
#                                                                                 
#   b_j = 1 for long month, b_j = 0 for short month                               
#   L is the leap month of the year if 1<=L<=12; NO leap month if L = 0.          
#   The leap month (if exists) is long one if M = 1.                              
yearCode = [                                                                      
                                            0x04bd8,        # 1900                    
    0x04ae0, 0x0a570, 0x054d5, 0x0d260, 0x0d950,        # 1905                    
    0x16554, 0x056a0, 0x09ad0, 0x055d2, 0x04ae0,        # 1910                    
    0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540,        # 1915                    
    0x0d6a0, 0x0ada2, 0x095b0, 0x14977, 0x04970,        # 1920                    
    0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, 0x1ab54,        # 1925                    
    0x02b60, 0x09570, 0x052f2, 0x04970, 0x06566,        # 1930                    
    0x0d4a0, 0x0ea50, 0x06e95, 0x05ad0, 0x02b60,        # 1935                    
    0x186e3, 0x092e0, 0x1c8d7, 0x0c950, 0x0d4a0,        # 1940                    
    0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0,        # 1945                    
    0x092d0, 0x0d2b2, 0x0a950, 0x0b557, 0x06ca0,        # 1950                    
    0x0b550, 0x15355, 0x04da0, 0x0a5d0, 0x14573,        # 1955                    
    0x052d0, 0x0a9a8, 0x0e950, 0x06aa0, 0x0aea6,        # 1960                    
    0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260,        # 1965                    
    0x0f263, 0x0d950, 0x05b57, 0x056a0, 0x096d0,        # 1970                    
    0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4, 0x0d250,        # 1975                    
    0x0d558, 0x0b540, 0x0b5a0, 0x195a6, 0x095b0,        # 1980                    
    0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50,        # 1985                    
    0x06d40, 0x0af46, 0x0ab60, 0x09570, 0x04af5,        # 1990                    
    0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58,        # 1995                    
    0x055c0, 0x0ab60, 0x096d5, 0x092e0, 0x0c960,        # 2000                    
    0x0d954, 0x0d4a0, 0x0da50, 0x07552, 0x056a0,        # 2005                    
    0x0abb7, 0x025d0, 0x092d0, 0x0cab5, 0x0a950,        # 2010                    
    0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0,        # 2015                    
    0x0a5b0, 0x15176, 0x052b0, 0x0a930, 0x07954,        # 2020                    
    0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6,        # 2025                    
    0x0a4e0, 0x0d260, 0x0ea65, 0x0d530, 0x05aa0,        # 2030                    
    0x076a3, 0x096d0, 0x04bd7, 0x04ad0, 0x0a4d0,        # 2035                    
    0x1d0b6, 0x0d250, 0x0d520, 0x0dd45, 0x0b5a0,        # 2040                    
    0x056d0, 0x055b2, 0x049b0, 0x0a577, 0x0a4b0,        # 2045                    
    0x0aa50, 0x1b255, 0x06d20, 0x0ada0                    # 2049                    
]                                                                                 
yearsCoded = len(yearCode)                                                        
                                                                                
                                                                                   
from sys import argv, exit, stdout                                                
from time import time, localtime                                                  
ow=stdout.write                                                                   
                                                                                
                                                                                
                                                                                
class LunarYearInfo:                                                              
    def __init__(self):                                                           
        self.yearDays = 0                                                         
        self.monthDays = [0]*13                                                   
        self.leapMonth = -1  # -1 means no lunar leap month                       
                                                                                
yearInfo = [0]*yearsCoded #global variable  
for i in range(yearsCoded):                                                       
    yearInfo[i] = LunarYearInfo()                                                 
                                                                                
                                                                                
                                                                                
class Date:                                                                       
    def __init__(self, year, month, day, weekday=-1, gan=-1, zhi=-1):             
        self.year   =year                                                         
        self.month  =month                                                        
        self.day    =day                                                          
        self.weekday=weekday                                                      
        self.gan    =gan                                                          
        self.zhi    =zhi                                                          
                                                                                
solar1st = Date(0, 0, 30, weekday=2)   #Wednesday, January 31, 1900               
lunar1st = Date(0, 0, 0,  weekday=2, gan=6, zhi=0)                                
#Wednesday, First day, First month, 1900, 庚子年                                  
                                                                                
                                                                                
                                                                                
def error(msg):                                                                   
    print 'Error:', msg; exit(0)                                                  
                                                                                
                                                                                
                                                                                
def isSolarLeapYear (year):                                                       
    year=year+1900                                                                
    return (year%4 == 0) and (year%100 != 0) or (year%400 == 0)                   
                                                                                
                                                                                
                                                                                
baseYear=1201 - 1900                                                              
# in fact, real baseYear=1201.  In order to ease calculation of                   
# leap years. real baseYear must conform to:                                      
#   realBaseYear%4==1 and realBaseYear%400==1.                                    
# Assert realBaseYear < solar1st.year .                                           
                                                                                
# Compute the number of days from the Solar First Date                            
# month=0 means January, ...                                                      
def solarDaysFromBaseYear(d):    #d is a Date class                               
    delta = d.year - baseYear                                                     
    offset = delta*365 + delta/4 - delta/100 + delta/400                          
    for i in range(d.month):                                                      
        offset += daysInSolarMonth[i];                                            
    if d.month>1 and isSolarLeapYear(d.year):                                     
        offset += 1                                                               
    offset += d.day                                                               
##   print '___', year, month, day, 'offset=', offset ########                    
    return offset                                                                 
                                                                                
# Compute the number of days from the Solar First Date                            
# month=0 means January, ..., year=0 means 1900, ...                              
def solarDaysFromFirstDate (d): #d is a Date class                                
    return solarDaysFromBaseYear (d) - solarDaysFromBaseYear (solar1st)           
                                                                                
                                                                                
                                                                                
def calcLunarDaysPerMonth(iYear):                                                 
    code = yearCode[iYear]                                                        
    leapMonth = code&0xf #leapMonth==0 means no lunar leap month                  
                                                                                
    code >>= 4                                                                    
    for iMonth in range(12):                                                      
        yearInfo[iYear].monthDays[11-iMonth] = lunarMonthDays [code&0x1]          
        code >>= 1                                                                
                                                                                
    if leapMonth>0:                                                               
        yearInfo[iYear].leapMonth = leapMonth-1                                   
        yearInfo[iYear].monthDays.insert (leapMonth,                              
                lunarMonthDays [code & 0x1])                                      
                                                                                                                                                                                                                                                   
def calcAllLunarYearsInfo():                                                      
    for iYear in range(yearsCoded):                                               
        calcLunarDaysPerMonth (iYear)                                             
        for iMonth in range(13):                                                  
            yearInfo[iYear].yearDays += yearInfo[iYear].monthDays[iMonth]         
                                                                                
                                                                                
                                                                                
                                                                                
#input dateSolar, return (dateLunar, isLunarMonthOrNot)                           
def solar2Lunar(d): #d is a Date class                                            
    dLunar = Date(-1, -1, -1) #unknown lunar Date class                           
                                                                                
    offset = solarDaysFromFirstDate(d)                                            
                                                                                
    dLunar.weekday  = (offset + solar1st.weekday)%7                               
                                                                                
    for iYear in range(yearsCoded):                                               
        if offset < yearInfo[iYear].yearDays:                                     
            dLunar.year = iYear; break                                            
        offset -= yearInfo[iYear].yearDays                                        
    if dLunar.year == -1:   error ("Date out of range.")                          
                                                                                
    dLunar.gan      = (dLunar.year + lunar1st.gan) % 10                           
    dLunar.zhi      = (dLunar.year + lunar1st.zhi) % 12                           
                                                                                
    for iMonth in range(13):                                                      
        if offset< yearInfo[dLunar.year].monthDays[iMonth]:                       
            dLunar.month = iMonth; break                                          
        offset -= yearInfo[dLunar.year].monthDays[iMonth]                         
                                                                                
    dLunar.day = offset                                                           
                                                                                
    isLeapMonth=0                                                                 
    if yearInfo[dLunar.year].leapMonth >=0:                                       
        if dLunar.month ==  yearInfo[iYear].leapMonth + 1:                        
            isLeapMonth=1                                                         
        if dLunar.month > yearInfo[dLunar.year].leapMonth:                        
            dLunar.month -= 1                                                     
                                                                                
    return (dLunar, isLeapMonth)   
                                                                                
                                                                                
                                                                                
def getSolarDaysInMonth (year, month):                                            
    if isSolarLeapYear(year) and month==1:                                        
            return 29                                                             
    else:   return daysInSolarMonth[month]                                        
                                                                                
                                                                                
def num2GB (num):                                                                 
    if num==10:                                                                   
        return '十'                                                               
    elif num>10 and num<20:                                                       
        return '十' + numGB[num-10]                                               
                                                                                
    tmp=''                                                                        
    while num>10:                                                                 
        tmp = numGB[num%10] + tmp                                                 
        num = int(num/10)                                                         
    tmp = numGB[num] + tmp                                                        
    return tmp                                                                    
                                                                                
                                                                                
def lunarDate2GB (dLunar, isLeapMonth):                                           
    tmp = str(dLunar.month)+'_'+str(dLunar.day)                                   
    if lunarHoliday.has_key( tmp ):                                               
        return '%s  '% lunarHoliday[tmp] + ' '*(6-len(lunarHoliday[tmp]))                                     
    elif dLunar.day==0:                                                           
        tmp2 = '闰'*isLeapMonth + num2GB(dLunar.month+1) +'月'                    
        return '%s' % tmp2 + ' '*(8-len(tmp2))                                    
    elif dLunar.day<10:                                                           
        return '初' + num2GB(dLunar.day+1)                                        
    else:                                                                         
        return num2GB(dLunar.day+1)                                               
                                                                                
                                                                                
def outputCalendar(year, month):                                                  
    dLunar = Date(-1,-1,-1)                                                       
    ow ('\n     阳历%d年%d月         ' % (year+1900, month+1) )                   
                                                                                
    for iDay in range( getSolarDaysInMonth(year, month) ):                        
        dSolar = Date(year, month, iDay)                                          
        dLunar, isLeapMonth = solar2Lunar (dSolar)                                
                                                                                
        if iDay==0:                                                               
            ow ('始于 阴历%s年%s%s月 (%s%s年, 生肖属%s)\n' %                      
                ( num2GB(dLunar.year+1900), '闰'*isLeapMonth,                     
                  num2GB(dLunar.month+1),                                         
                ganGB [dLunar.gan], zhiGB[dLunar.zhi], shengXiaoGB[dLunar.zhi]  
                ))                                                                
            ow ('='*74 + '\n')                                                    
            for i in range(7):                                                    
                ow ("%3s %2s     " % (weekdayEn[i][:3], weekdayGB[i]) )           
            ow('\n\n')                                                            
            for i in range(dLunar.weekday): ow(' '*11)                            
                                                                                
        elif dLunar.weekday==0: ow('\n')                                          
                                                                                
        ow ( "%2d %-8s" %(iDay+1, lunarDate2GB(dLunar, isLeapMonth) ) )           
    ow('\n\n')                                                                    
                                                                                
                                                                                
                                                                                
                                                                                
def checkArgv (argv):                                                             
    argc = len(argv)                                                              
    if argc==1 or argv[1] in ('-h', '--help'):                                    
        print __doc__; exit(0)                                                    
                                                                                
    #in case people input arguments as "4-digit-year month"                       
    if argc==3 and len(argv[1]) == 4 and len(argv[2]) in (1,2):                   
        argv[1], argv[2] = argv[2], argv[1]                                       
                                                                                
                                                                                
    #Get month                                                                    
    month=-1                                                                      
    for iMonth in range(12):                                                      
        if argv[1].lower() == monthEn[iMonth].lower() or argv[1].lower() == monthEn[iMonth][:3].lower():                        
            month = iMonth+1; break                                            
    if month==-1:                                                                 
        month = eval(argv[1])                                                     
                                                                                
    if month<1 or month>12:     error ("Month not within 1--12.")                 
                                                                                
    #Get year                                                                     
    if argc==2: year = localtime(time())[0]                                       
    else:                                                                         
        if len(argv[2]) != 4:   error ("Year must be 4 digits.")                  
        year = eval(argv[2])                                                      
        if year<1900 or year>= 1900+yearsCoded or (year==1900 and month==1):      
            error ("Year must be within %d--%d, excluding 1900/1."                
                    % (1900, 1900 + yearsCoded-1) )                               
                                                                                
    return year-1900, month-1                                                     
                                                                                
year, month = checkArgv(argv)                                                     
calcAllLunarYearsInfo()                                                           
outputCalendar(year, month)                                                       