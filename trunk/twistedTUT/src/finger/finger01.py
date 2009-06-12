#coding=utf-8
'''
    拒绝连接(Refuse Connections)
    这个例子只运行了反应器(reactor)。所以什么也不会发生。它几乎不会耗费任何处理器(cpu)资源。也许没什么用，不过这是Twisted程序成长的骨架。 
    不是你的程序调用Twisted，而是Twisted来调用你的程序。反应器是Twisted的主事件循环。每一个运行着的Twisted程序都有一个反应器，一旦启动它，它就不停循环，响应网络事件，然后执行预定的调用。 
'''

from twisted.internet import reactor
reactor.run()