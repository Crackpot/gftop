#coding=utf-8
def foo(debug=True):    #默认参数
    if debug:
        print '默认参数debug为True\t调试模式'
    else:
        print '默认参数的值被改变为False\t非调试模式'
    
foo()
foo(False)