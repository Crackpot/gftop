#!/usr/bin/env python
#coding=utf-8
'makeTestFile.py -- 创建文本文件'
import os
ls=os.linesep
#获取文件名
fname=raw_input('请输入文件名')
while True:
    if os.path.exists(fname):
        print '错误："文件%s"已经存在'%fname
    else :
        break
#获取文件内容
all=[]
print '请输入文件内容(输入"."时结束)'
while True:
    entry=raw_input('>')
    if entry=='.':
        break
    else:
        all.append(entry)
#向文件写入内容
fobj=open(fname,'w')
fobj.writelines(['%s %s'%(x,ls)for x in all])
fobj.close()
print '完成'
    