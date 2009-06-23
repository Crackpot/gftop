#!/usr/bin/env python
#coding=utf-8
li = ["Larry", "Curly"]
print  "li=",li
print "\n".join(["执行的操作%s\t操作元素：%s\t\t操作后li的元素是%s"%("li.pop()",li.pop(),li)])   #这样得到列表的 pop 方法的一个引用。注意这样不是调用 pop 方法，调用应是 li.pop()。它是方法本身。
print "getattr(li,\"pop\")\t\t",getattr(li, "pop") #这样也返回 pop 方法的引用，但这次，方法的名字被指定为 getattr 函数的一个字符串参数。 getattr 是一个相当有用的内置函数，它可以返回任意对象的任意属性。在本例中，对象是列表，属性是 pop 方法。
print "getattr(li,\"append\")(\"Moe\")\t",getattr(li, "append")("Moe")  #getattr 的返回值是方法，接着你可以调用它就好象直接调用 li.append("Moe")。但是你没有直接调用函数，而是把函数名当成字符串来指定。
print "li=",li
print "getattr({},\"clear\")\t ",getattr({}, "clear")   #getattr 也可以用于字典。
#getattr((), "pop") 此操作会出错.    在理论上，getattr 应可以用于序列，除了序列没有方法，所以不管给出什么属性名， getattr 都将引发一个异常。
import odbchelper
print "odbchelper.buildConnectionString\t",odbchelper.buildConnectionString     #它返回在 odbchelper 模块中的 buildConnectionString 函数的引用， odbchelper 模块我们在开始了解Python中学过了。(你看到的16进制地址是专对我的机器的；你的输出将有所不同。)
object=odbchelper
method="buildConnectionString"
print "getattr(object, method)\t",getattr(object, method)
print "type(getattr(object, method))\t",type(getattr(object, method))  
import types
print "type(getattr(object, method))==types.FunctionType\t",type(getattr(object, method))==types.FunctionType