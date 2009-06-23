#!/usr/bin/env python
#coding=utf-8

li1=[1,9,8,4]    #创建一个列表
print "创建的列表li1为：",li1
li2=[elem*2 for elem in li1] #创建一个新的列表，将列表li中每个元素的2倍赋值给列表li2
print "列表li2为：",li2
print "列表li1为：",li1
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"} #创建一个字典
print "字典params为：",params
print "通过params.keys()输出键名：",params.keys() #输出键名
print "用语句print [k for k in params.keys()]输出键名：",[k for k in params.keys()]    #同样输出键名。简单的列表映射举例。映射表达式刚好是元素自身，所以这个列表映射返回列表的原封不动的拷贝。它等于 params.keys().
print "用print [params[k] for k in params.keys()]输出字典中的各个键值：",[params[k] for k in params.keys()]
print "用语句print [\"%s=%s\" %(k,params[k])for k in params.keys()]按照指定格式输出键名与键值：",["%s=%s" %(k,params[k])for k in params.keys()]