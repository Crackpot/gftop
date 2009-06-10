#coding=utf-8
'''
    通常，应用程序会把模板用文本文件的形式保存在文件系统中。而为了方便起见，我们可以直接通过 TemplateLookup 来获取模板对象，利用 TemplateLookup 的 get_template 方法，并传递模板的 URI 作为参数
    lookup 在查找模板时通过向其中的每一个搜索路径附加我们提供的模板 URI 的方式，来尝试获取模板文件。如果找不到则引发 TopLevelNotFound 异常，这是一个 Mako 的自定义异常类型。
    当 lookup 找到模板时，它还会给 Template 指定一个 uri 属性，这个 uri 就是传递给 get_template() 方法的参数。Template 可以用此 uri 来计算出其对应的模块文件的名称。比如在上述例子中，/etc/beans/info.txt 这个 URI 名称参数，会导致创建模块文件 /tmp/mako_modules/etc/beans/info.txt.py.
'''
from mako.template import Template
from mako.lookup import TemplateLookup

#mylookup=TemplateLookup(directories=['/home/workspace/gftop/MakoLearning/src/BasicUsage/docs'],module_directory='/home/workspace/gftop/MakoLearning/src/BasicUsage/mako_modules')
'''TemplateLookup 同时也会在内存中缓存一组模板，所以并不是每一次请求都会导致模板的重新编译和模块重新加载。默认 TemplateLookup 的大小没有限制，但可以通过 collection_size 参数来限制它。此时的lookup 会持续加载模板到内存中，直到达到 500 的时候，它就会清除掉一定比例的模板缓存项，根据“最近最少访问”原则。'''
mylookup=TemplateLookup(
    directories=['/home/workspace/gftop/MakoLearning/src/BasicUsage/docs'],
    module_directory='/home/workspace/gftop/MakoLearning/src/BasicUsage/mako_modules',
    collection_size=500,
    #filesystem_checks=True,
)
'''
    设置文件系统检查
    另一个 TemplateLookup 相关的标志是  filesystem_checks. 默认为 True, 每一次 get_template() 方法返回模板后，原始的模板文件的 revision time 会和上次加载模板的时间做对比，如果文件更新，则会加载其内容，并重新编译该模板。在生产环境下，设置 filesystem_checks 为 False 可以带来一定的性能提升（和具体的文件系统有关）。
'''

def server_template(templatename,**kwargs):
    mytemplate=mylookup.get_template(templatename)
    print mytemplate.render(**kwargs)
server_template('mytmpl.txt',name=u'高飞',sex=u'男',age=23,)
