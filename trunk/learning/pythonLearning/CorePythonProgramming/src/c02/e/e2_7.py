#coding=utf-8
string='I love China'
def funcWhile():
    print '用while逐字显示字符串'
    i=0
    while i<len(string):
        print string[i]
        i+=1
def funcFor():
    print '用for逐字显示字符串'
    for i in string:
        print i
        
funcWhile()
funcFor()