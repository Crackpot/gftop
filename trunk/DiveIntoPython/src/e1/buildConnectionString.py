#!/usr/bin/env python
#coding=utf-8

import odbchelper   #将 odbchelper 程序作为模块导入。一旦你导入一个模块，你可以引用它的任何的公共函数，类，或属性。
print "odbchelper模块的__name__属性为：", odbchelper.__name__
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
#使用定义在被导入模块中的函数时，必须包括模块的名字。
print  "函数的参数", odbchelper.buildConnectionString(params)  #输出函数的参数
print "函数的文档字符串", odbchelper.buildConnectionString.__doc__  #输出函数的文档字符串