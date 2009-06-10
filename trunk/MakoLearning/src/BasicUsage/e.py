#coding=utf-8
'''
    使用 TemplateLookup
    在模板中，我们有时候需要调用或引用其他模板的内容，这就牵涉一个模板查找定位的问题，通常用简单的 URI 字符串来定位。
    我们用 TemplateLookup 类来负责这个任务。
    该类的构造函数需要传递一系列可供查找模板的路径的列表。然后我们再将此 TemplateLookup 对象用关键字参数的形式传递给 Template 对象。
    创建了一个文本模板，其中有一个对 header.txt 文件的包含引用。而从何处去查找 header.txt, 则由 TemplateLookup 指明，是 "docs" 目录。 
'''
from mako.template import Template
from mako.lookup import TemplateLookup
mylookup=TemplateLookup(directories=['/home/workspace/gftop/MakoLearning/src/BasicUsage/docs'])
mytemplate=Template(
    """<%include file="header.txt"/>\nhello world!""",
    lookup=mylookup
)
print mytemplate.render()

