#coding=utf-8
def displayNumType(num):
    print num,'is：'
    if isinstance(num, (int,long,float,complex)):
        print 'a number of type',type(num).__name__
    else:
        print 'not a number at all!'
def displayNumType2(num):
    print num,'is:'
    if type(num)==type(0):
        print 'an integer'
    elif type(num)==type(0L):
        print 'a long'
    elif type(num)==type(0.0):
        print 'a float'
    elif type(num)==type(0+0j):
        print 'a complex number'
    else:
        print 'not a number at all!'
displayNumType2(-79)
displayNumType2(99999999999999999999999999999999L)
displayNumType2(98.8)
displayNumType2(-4.3+3.2j)
displayNumType2('xxx')

import types
num='haha'
if type(num)==types.IntType:
    print '整型'
elif type(num)==types.StringType:
    print '字符串型'
else:
    pass
    