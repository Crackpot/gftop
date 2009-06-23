#!/usr/bin/env python
#coding=utf-8

import fileinfo

#__getitem__ 专用方法
def __getiem__(self,key):
    return self.data[key]

f=fileinfo.FileInfo("/home/crackpot/Music/westlife/against all odds.mp3")
print f 
print f.__getitem__("name")     #__getitem__ 专用方法很简单。象普通的方法 clear，keys，和 values一样，它只是重定向到字典，返回字典的值。但是怎么调用它呢？哦，你可以直接调用 __getitem__，但是在实际中你其实不会那样做：我在这里执行它只是要告诉你它是如何工作的。正确地使用 __getitem__ 的方法是让Python来替你调用。
print f["name"]     #这个看上去就象你用来得到一个字典值的语法，事实上它返回你期望的值。下面是隐藏起来的一个环节：暗地里，Python已经将这个语法转化为 f.__getitem__("name") 的方法调用。这就是为什么 __getitem__ 是一个专用类方法的原因，不仅仅是你可以自已调用它，还可以通过使用正确的语法让Python来替你调用。

#__setitem__ 专用方法
def __setitem(self,key,itrm):       #象 __getitem__ 方法一样， __setitem__ 简单地重定向到真正的字典 self.data ，让它来进行工作。并且象 __getitem__ 一样，通常你不会直接调用它，当你使用了正确的语法，Python会替你调用 __setitem__ 。
    self.data[key]=item
print f 
print f.__setitem__("crackpot", 23)
print f 
f["crackpot"]=23        #这个看上去象正常的字典语法，当然除了 f 实际上是一个类，它尽可能地打扮成一个字典，并且 __setitem__ 是打扮的一个重点。这行代码实际上暗地里调用了 f.__setitem__("genre", 32)。
print f 

#__setitem__ 是一个专用类方法，因为它可以让Python来替你调用，但是它仍然是一个类方法。就象在 UserDict 中定义 __setitem__ 方法一样容易，我们可以在子类中重新定义它，对父类的方法进行覆盖。这就允许我们定义出在某些方面象字典一样动作的类，但是可以定义它自已的行为，超过和超出内置的字典。