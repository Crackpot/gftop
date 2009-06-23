#!/usr/bin/env python
#coding=utf-8

li=[]
print "dir(li)\t\t",dir(li) #li 是一个列表，所以 dir(li) 返回列表所有方法的一个列表。注意返回的列表包含着字符串表示的方法的名字，而不是方法自身。
d={}
print "dir(d)\t\t",dir(d)   #['clear', 'copy', 'get', 'has_key', 'items', 'keys', 'setdefault', 'update', 'values']
import odbchelper
print "dir(odbchelper)\t\t",dir(odbchelper) #这里就是真正变得有趣的地方。odbchelper 是一个模块，所以 dir(odbchelper) 返回在模块中定义的所有东西的列表，包括内置属性，象 __name__ 和 __doc__，和你定义的属性和方法其它什么的。在这个例子中，odbchelper 仅有一个用户自定义方法，buildConnectionString 函数，我们在开始了解Python中学过的。

#type，str，dir，和所有其它的Python内置函数被组合进一个名叫 __builtins__ 的特别模块中。(它在前后有两个下划线。)如果有帮助的话，你可以认为Python在启动时自动地执行 from __builtins__ import * ，这样就导入了所有内置的函数到名字空间中，所以你可以直接使用它们。
#象这样考虑的好处是，你可以通过得到 __builtins__ 的信息，作为一个组，存取所有内置的函数和属性。猜到什么了吗？我们有一个实现那个功能的函数，它叫做 help。自已试一下然后现在完全忽略列表；在后面我们将深入到一些更重要的功能。(一些内置错误类，象 AttributeError，应该看上去已经熟悉了。)