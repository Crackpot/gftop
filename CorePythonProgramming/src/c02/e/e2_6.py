#coding=utf-8
import random
#i=random.randrange(-32767,32768)
#print '系统随机产生的数字为：%d'%i
try:
    i=int(raw_input('请输入一个数字'))
    if i<0:
        print '负数'
    elif i==0:
        print '零'
    else:
        print '正数'
except Exception,e:
    print '您输入的值不正确'
