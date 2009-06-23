#!/usr/bin/env python
#coding=utf-8

#定义一个字典
d={"server":"mpilgrim","database":"master"} #首先，我们创建了一个拥有两个元素的新字典，并将其赋值给变量 d。每一个元素都是一个键-值对，整个元素集合用大括号括起来。
print d 
print d["server"]   #server 是一个键字，它所关联的值为 mpilgrim，用 d["server"] 来引用。
print d["database"] #database 是一个键字，它所关联的值为 master，用 d["database"] 来引用。
#print d["mpilgrim"]    执行此语句会出错，可以通过键字来得到值，但是不能通过值得到键字。
print "修改一个字典"
print d
d["database"]="pubs"    #不能在一个字典中有重复的键字。给一个存在的键字赋值会抹掉原来的值。
print d
d["uid"]="sa"   #可以在任何时候加入新的键-值对。这种语法同修改存在的值一样。(是的，它可能某天会给你带来麻烦，你可能认为增加了新值，但实际上只是反复地修改了同样的值，因为你的键字没有按照你的想象改变。)
print d #新的元素(键字为 uid，值为 sa)出现在字典中间。实际上，它只不过是一种巧合，在第一个例子中的元素看上去是有序的。现在它们看上去无序了则更是一种巧合。
#字典没有元素顺序的概念。说元素顺序乱了是不正确的，它们只是简单的无序。这是一个重要的特性，它会在你想要以一种特定的，可重复的顺序(象以键字的字母表顺序)存取字典元素的时候骚扰你。有一些实现的方法，它们只是没有加到字典中去。
print "在字典中混用数据类型"
d["retrycount"]=3   #字典不是只用于字符串。字典的值可以是任意数据类型，包括字符串，整数，对象，或者甚至其它的字典。在一个单个字典里，字典的值并不需要全都是同一数据类型，可以根据需要混用和配匹。
print d
d[42]="douglas" #字典的关键字要严格一些，但是它们可以是字符串，整数和几种其它的类型(后面还会谈到这一点)。也可以在一个字典中混用和配匹关键字。
print d
print "从字典中删除元素"
print "删除键字为42的那一项"
del d[42]
print d 
print "清空字典"
d.clear()
print '字典d中的内容：',d 
d={
   '今天天气':'晴朗',
   '心情':'不错'
   }
print d
print '通过对字典的解释将中文内容输出:'
for k,v in d.items():       #通过对字典的解释将中文内容输出
    print 'Key:',k,'\tValue:',v