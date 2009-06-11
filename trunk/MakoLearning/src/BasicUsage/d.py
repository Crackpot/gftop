#coding=utf-8
'''
    使用基于文件的模板
    可以从文件中加载 Template 的内容，使用 filename 关键字参数 
'''
from mako.template import Template

#mytemplate=Template(filename='/home/workspace/gftop/MakoLearning/src/BasicUsage/docs/mytmpl.txt')
'''
    为提高性能，从文件中加载的 Template, 可以将它产生的模块的源代码以普通 python 模块文件的形式(.py)，缓存到文件系统中。只要加一个参数 module_directory 即可做到这一点：
'''
mytemplate=Template(
    filename='/home/workspace/gftop/MakoLearning/src/BasicUsage/docs/mytmpl.txt',
    module_directory='/home/workspace/gftop/MakoLearning/src/BasicUsage/mako_modules'
)

print mytemplate.render(        #中文问题遗留
    name=u'高飞',
    sex=u'男',
    age=23,
)
