#coding=utf-8
print "动态得到文档字符串："
import odbchelper
object=odbchelper   #在 help 函数中，object 是我们正要得到帮助的对象，它被作为一个参数传进来。
method="buildConnectionString"  #当我们遍历 methodList，method 是当前方法的名字。
print "getattr(object, method)\t\t",getattr(object, method) #通过使用 getattr 函数，我们得到在 object 模块中对于 method 函数的一个引用。
print "getattr(object, method).__doc__:\t%s\n%s\n"%("打印文档字符串",getattr(object, method).__doc__)  #现在，打印出方法的文档字符串很容易。

print "为什么对一个文档字符串使用 str ？"
print {}.keys.__doc__
print {}.keys.__doc__==None
print str({}.keys.__doc__)

print "ljust 方法介绍:\nljust 用空格填充字符串到指定长度。help 函数就是用它用来生成两列输出数据，并且将所有在第二列的文档字符纵向对齐。"
s="buildConnectionString"
print "%s%s%s%s"%("字符串",s,"的长度为：",len(s))
print "%s%s"%(s.ljust(30),".--s.ljust(30)")
print "%s%s"%(s.ljust(20),".--s.ljust(20)\t如果给定的长度小于字符串的长度，ljust 将简单地返回未变化的字符串。它决不会截断字符串。")

print "打印列表："
li=['a','b','c']
print "\t".join(li)