#!/usr/bin/env python
#coding=utf-8
print "type(1):\t\t",type(1)    #type 接收任何事物，并且返回它的数据类型。我的意思是任何东西。整数，字符串，列表，字典，序列，函数，类，模块，甚至类型。
li=[]
print "type(li):\t\t",type(li)  #type 可以接收变量并返回它的数据类型。
import odbchelper
print "type(odbchelper)\t\t",type(odbchelper)   #type 也可以用于模块。
import types    #可以使用 types 模块中的常量用来比较对象的类型。这就是 help 函数所做的，这一点很快会看到。
type=(odbchelper)==types.ModuleType
print "odbchelper类型是模块类型么？",type