#!/usr/bin/env python
#coding=utf-8
import odbchelper
print "str(1)",str(1)    #对于象整数这样的简单类型，你会认为 str 可以工作，因为几乎每一种语言都有一个用来将整数据转化为字符串的函数。
horsemen = ['war', 'pestilence', 'famine']
print horsemen
print "在列表的尾部添加元素"
horsemen.append('Powerbuilder')
print horsemen
print "str(horsemen):\t\t",str(horsemen) #然而 str 可工作于任何类型的任何对象。这里它应用于一个我们零碎构造的列表。
print "str(odbchelper)\t\t",str(odbchelper)   #str 也可用于模块。注意，模块的字符串表示包含了模块在磁盘上的路径，所以你的结果看上去可能不一样。
print "str(None)",str(None) # str 的一个细小但很重要的行为是它可以用于 None，Python空值。它返回字符串 'None'。我们将应用这一点在 help 函数中来满足我们的需要，这一点我们很快会看到。