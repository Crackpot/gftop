#!/usr/bin/env python
#coding=utf-8

"""
    连接列表与分割列表
"""
print "连接列表："
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print ["%s=%s"%(k, params[k])for k in params.keys()]
print ";".join(["%s=%s"%(k, params[k])for k in params.keys()])
li=['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s=";".join(li)
print s
print "分割字符串："
print s.split(";")  #split 与 join 相反，通过将一个字符串分割成多元素列表。注意，分隔符(“;”)被完全去掉了，它没有在返回的列表中的任意元素中出现。
print s.split(";", 1)   #split 接受一个可选的第二个参数，它是要分割的次数。(哦，可选参数...你将会在下一章中学会如何在你自已的函数中实现它。)
#string.split(delimiter, 1) 是一个有用的技术，在你想要搜索一个子串，然后处理字串前面的东西(即列表中第一个元素)和其后的东西(即列表中第二个元素)时，使用这个技术。
