#coding=utf-8
'''
    template.render() 方法会让 Mako 创建一个 Context 对象，其中包含了所有该模板可访问的变量的名称，以及一个用于捕获输出的缓冲区。你也可以自己创建 Context 对象，并命令模板利用此 Context 来 render，用 render_context 方法即可
'''
from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO

mytemplate=Template('hello,${name}!')
buf=StringIO()
ctx=Context(buf,name='crackpot')
mytemplate.render_context(ctx)
print buf.getvalue()
