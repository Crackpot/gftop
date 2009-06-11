#coding=utf-8
'''
    render_body() 函数中的代码可以访问包含了一些变量的一个名称空间。你可以传递额外的关键字参数给 render() 方法，这些参数将转化为可被访问的变量
'''
from mako.template import Template
mytemplate=Template("hello,${name}!")
print mytemplate.render(name="Crackpot")        #中文问题遗留
