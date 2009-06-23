#!/usr/bin/env python
#coding=utf-8

#缩排表示块的开始，非缩排表示结束，不存在明显的括号，大括号，或关键字。
def buildConnectionString(params):  #声明 buildConnectionString 函数    关键字 def 为函数声明的开始

    #三重双引号的引用表示一个多行字符串
    """Build a connection string from a dictionary of parameters.  



    Returns string."""

    return ";".join(["%s=%s" % (k, params[k]) for k in params.keys()])  #返回值。中间部分“"%s=%s" % (k, params[k])”是字符串格式化表达式。
    #for k in params.keys()         字典params中的所有键名


#在 if 表达式周围不需要小括号。象C语言一样，Python使用 == 进行比较
if __name__ == "__main__":      
    #所有的模块都有一个内置属性 __name__。一个模块的 __name__ 的值要看你如何使用它。如果 import 模块，那么 __name__ 的值通常为模块的文件名，不带路径或者文件扩展名。但是你也可以象一个标准的程序一样直接运行模块，在这种情况下 __name__ 的值将是一个特别的缺省值， __main__。

#定义 myParams 变量（它是一个字典）
    myParams = {"server":"mpilgrim", \

                "database":"master", \

                "uid":"sa", \

                "pwd":"secret" \

                }
#变量的赋值是一条命令被分成了几行，用反斜线(“\”)作为续行符。
#当一条命令用续行符(“\”)分割成多行时，后续的行可以以任何方式缩排，Python通常的严格的缩排规则不需遵守。如果你的Python IDE自由对后续行进行了缩排，你应该把它当成是缺省处理，除非你有特别的原因不这么做。
#严格地讲，在小括号，方括号或大括号中的表达式(如定义字典)可以用或者不用续行符(“\”)分割成多行。甚至在不必需的时候，我也喜欢包括反斜线，因为我认为这样会让代码读起来容易，但那只是风格的问题。

    print buildConnectionString(myParams)

