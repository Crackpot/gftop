#!/usr/bin/env python
#coding=utf-8

from fileinfo import FileInfo
def __setitem__(self,key,item):     #__setitem__ 方法严格按照父类方法相同的形式进行定义。这一点很重要，因为Python将替你执行方法，则它希望这个函数用确定个数的参数进行定义。(从技术上说，参数的名字没有关系，只是个数。)
    if key=="name" and item:        #这里就是整个 MP3FileInfo 类的难点：如果给 name 关键字赋一个值，我们还想做些额外的事情。
        self.__parse(itrm)      # 我们对 name 所做的额外处理封装在了 __parse 方法中。这是定义在 MP3FileInfo 中的另一个类方法，则当我们调用它时，我们用 self 对其限定。仅是调用 __parse 将只会看成定义在类外的普通方法，调用 self.__parse 将会看成定义在类中的一个类方法。这不是什么新东西，你用同样的方法来引用数据属性。
    FileInfo.__setitem__(self, key, item)       #在做完我们额外的处理之后，我们需要调用父类的方法。记住，在Python中不会自动为你完成，需手工执行。注意，我们在调用直接父类， FileInfo，尽管它没有一个 __setitem__ 方法。没问题，因为Python将会沿着父类树走，直到它找到一个有着我们正在调用方法的类，所以这行代码最终会找到并且调用定义在 UserDict 中的 __setitem__。

#当在一个类中存取数据属性时，你需要限定属性名：self.attribute。当调用类中的其它方法时，你属要限定方法名：self.method。
import fileinfo
mp3file=fileinfo.MP3FileInfo()      #首先，我们创建了一个 MP3FileInfo 的实例，没有传递给它文件名。(我们可以不用它，因为 __init__ 方法的 filename 参数是可选的。)因为 MP3FileInfo 没有它自已的 __init__ 方法，Python沿着父类树走，发现了 FileInfo 的 __init__ 方法。这个 __init__ 方法手工调用了 UserDict 的 __init__ 方法，然后设置 name 关键字为 filename，它为 None，因为我们还没有传入一个文件名。所以，mp3file 最初看上去象有一个关键字， name，它的值为 None 的字典。
print mp3file
mp3file["name"]="/home/crackpot/Music/westlife/against all odds.mp3"        #现在真正有趣的开始了。设置 mp3file 的 name 关键字触发了 MP3FileInfo 上的 __setitem__ 方法(不是 UserDict)，这个方法注意到我们正在用一个真实的值来设置 name 关键字，接着调用 self.__parse。尽管我们完全还没有研究过 __parse 方法，从它的输出你可以看出，它设置了其它几个关键字：album，artist，genre，title，year，和 comment。  
print mp3file       #修改 name 关键字将再次经受同样的处理过程：Python调用 __setitem__，__setitem__调用 self.__parse，self.__parse 设置其它所有的关键字。