#coding=utf-8
from mako.template import Template
from mako.lookup import TemplateLookup

'''
    使用 Unicode 和 Encoding
    Template 和 TemplateLookup 都可以接受 output_encoding 和 encoding_errors 参数，用来对输出以 Python 支持的任何方式进行编码。 
'''
mylookup=TemplateLookup(
    directories=['/home/workspace/gftop/MakoLearning/src/BasicUsage/docs'],
    output_encoding='utf-8',
    encoding_errors='replace'
)
mytemplate=mylookup.get_template('mytmpl.txt')
print mytemplate.render(
    name=u'高飞',
    sex=u'男',
    age=23,
)
'''另外，render_unicode() 方法可以将模板的输出转换为一个 Python 的 Unicode 对象返回： '''
print mytemplate.render_unicode(
    name=u'高飞',
    sex=u'男',
    age=23,
)
'''上面的方法调用未提供编码参数，可以通过下面的语法进行编码'''
print mytemplate.render_unicode(
    name=u'高飞',
    sex=u'男',
    age=23,
).encode('utf-8','replace')
