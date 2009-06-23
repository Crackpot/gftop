#!/usr/bin/env python
#coding=utf-8
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print "li=", li
print "[elem for elem in li if len(elem)>1]\t", [elem for elem in li if len(elem)>1]    #这里的映射表达式很简单(它只返回每个元素的值)，所以把注意力集中到过滤表达式上。当Python遍历列表时，它对每个元素执行过滤表达式；如果过滤表达式为真，元素被映射且映射表达式的值被包括在返回列表中。这里你过滤掉了所有单个字符字符串，所以留下了一个都是长字符串的列表。
print "[elem for elem in li if elem!=\"b\"]\t", [elem for elem in li if elem!="b"]  #这里你过滤掉了一个特殊值 b。注意，它会过滤掉所有出现的 b 元素，因为每次 b 被取出来，过滤表达式将是假。
print "[elem for elem in li if li.count(elem)==1]\t",[elem for elem in li if li.count(elem)==1] #count 是列表的方法，它返回在一个值在列表中出现的次数。你也许会认为这个过滤将消除列表中的重值，返回一个只包含了在原始列表中有着唯一值拷贝的列表。但是不是这样的，因为在原始列表中出现两次的值(在本例中， b 和 d)被完全排除了。存在从一个列表排除重复值的方法，但是过滤不是解决办法。
