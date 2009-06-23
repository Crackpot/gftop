#!/usr/bin/env python
#coding=utf-8

print "and-or技巧(相当于bool ? a : b):"
a="first"
b="second"
print "a=%s"%a 
print "b=%s"%b
b="second"
print "1 and a or b\t",(1 and a or b)   #这个语法看起来与C语言中的 bool ? a : b 相似。第一部分将在布尔环境中进行计算，它可以是任意Python表达式。如果计算为真，整个表达式的值为 a。
print "0 and a or b\t",(0 and a or b)    #如果第一部分计算为假，整个表达示的值为 b。
print "and-or技巧失败:"
a=""
b="second"
print "a=\"\""
print "b=%s"%b
print "1 and a or b\t",1 and a or b
print "因为 a 是一个空串，空串在一个布尔环境中被Python看成假值，这个表达式将“失败”，且返回 b 的值。如果你不将它想象成象 bool ? a : b 一样的语法，而把它看成纯粹的布尔逻辑，这样的话就会得到正确的理解。 1 是真，a 是假，所以 1 and a 是假。假 or b 是 b。"
print "安全使用and-or技巧:"
a=""
b="second"
print "a=\"\""
print "b=%s"%b
c=(1 and [a] or [b])[0]
d="这个值为空字符串"
print "(1 and [a] or [b])[0]=\t%s\t%s"%(c,d)
print "因为 [a] 是一个非空列表，它永远不会为假。甚至 a 是 0 或 '' 或其它假值，列表 [a] 为真，因为它有一个元素。"
print "一个负责的程序员应该将 and-or 技巧封装成一个函数：\ndef choose(bool,a,b):\n    return (bool and [a] or [b])[0]"
def choose(bool,a,b):
    return (bool and [a] or [b])[0]
print "%s=%s\t%s"%("choose(1, a, b)",choose(1, a, b),"调用此函数所得的值仍然是一个空字符串")
