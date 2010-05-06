#!/usr/bin/env python
#coding=utf-8
'readTextFile.py -- 读取并显示文本文件'
fname=raw_input('请输入文件名称')
try:
    fobj=open(fname,'r')
except IOError,e:
    print '文件打开错误'
else:
    for eachline in fobj:
        print eachline
    fobj.close()    