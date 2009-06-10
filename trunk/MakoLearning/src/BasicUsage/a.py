#coding=utf-8
'''
    最简单的方法是通过Template类，创建模板并渲染它。
    传递给 Template 的文本参数被编译成了一个 python 的模块。
    该模块有一个 render_body() 函数，用于输出模板内容。
    当 mytemplate.render() 被调用时，Mako 会为此模板创建起一个运行时环境，并调用 render_body() 函数，然后捕获其输出到缓冲区，然后返回其字符串内容。
'''
from mako.template import Template
mytemplate=Template((unicode("哈哈")).encode('utf-8'))
print mytemplate.render()