#!/usr/bin/env python
#coding=utf-8
'用来比较两个对象的大小'
a,b=-4,12
print cmp(a, b)
print cmp(b, a)
b=-4
print cmp(a, b)
a,b='abc','xyz'
print cmp(a, b)
print cmp(b, a)
b='abc'
print cmp(a, b)