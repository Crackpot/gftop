#!/usr/bin/env python
#coding=utf-8

import fileinfo
f=fileinfo.FileInfo("/home/crackpot/Music/westlife/against all odds.mp3")       #在创建一个 FileInfo 类的实例(定义在 fileinfo 模块里)，将新创建的实例赋给变量 f。我们传入一个参数，/home/crackpot/Music/westlife/against all odds.mp3，它将结束就象在 FileInfo 中的 __init__ 方法的 filename 参数。
print f.__class__       #每一个类的实例有一个内置属性， __class__，它是对象的类。(注意这个表示包括了在我机器上的实例的物理地址，你的表示将是不一样的。)
print f.__doc__     #你可以存取实例的文档字符串，就象一个函数或模块。一个类的所有实例共享相同的文档字符串。
print f     #还记得 __init__ 方法将它的文件名参数赋值给 self["name"]吗？哦，答案在这。当我们创建类实例时，传递的参数从右向左发送给 __init__ 方法(跟着为对象的引用， self，它是由Python自动添上去的)。



print "尝试实现内存泄漏"
def leakmem():
    f=fileinfo.FileInfo('/home/crackpot/Music/westlife/against all odds.mp3')       #每次 leakmem 函数被调用，我们创建 FileInfo 的一个实例，将其赋给变量 f，这个变量是函数内的一个局部变量。然后函数结束未曾释放 f，所以你可能认为有内存泄漏，但是你错了。当函数结束时，局部变量 f 超出了作用域。在这个地方，不再有任何对 FileInfo 新创建实例的引用(因为除了 f 我们从未将其赋值给其它变量)，所以Python替我们破坏掉实例。

for i in range(100):
    leakmem()       #不管我们调用 leakmem 函数多少次，决不会泄漏内存，因为每一次，Python将在从 leakmem 返回前破坏掉新创建的 FileInfo 类。
    


#对于这种垃圾收集的方式，技术上的术语叫做“引用计数”。Python维护着对每一个创建的实例的引用的列表。在上面的例子中，对于 FileInfo 实例只有一个引用：局部变量 f。当函数结束时，变量 f 超出作用域，所以引用计数降为 0，则Python自动破坏实例。

#在Python的以前版本中，存在引用计数失败的情况，并且Python不能在你后面进行清除。如果你创建两个实例，它们相互引用(例如，双重链表，每一个结点有都一个指向列表中前一个和后一个结点的指针)，任一个实例都不会被自动破坏，因为Python(正确)认为对于每个实例都存在一个引用。 Python 2.0有一种额外的垃圾回收方式，叫做“标记后清除”，它足够聪明，可以正确地清除循环引用。

#由于以前学过的哲学课，让我困扰的是思考当事物没有人观察它的时候，它消失了，但是这确实是在Python中所发生的。通常，你可以完全忘记内存管理，让Python在你后面进行清除。
    