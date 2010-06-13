#coding=utf-8
'''
http://www.pythonchallenge.com/pc/return/uzi.html
'''
from calendar import weekday
for n in range(0,100):
    if weekday(1006+n*10, 1, 26)==0:    #1月26号是星期一，从一到日是从0到6
        print (1006+n*10,1,26)