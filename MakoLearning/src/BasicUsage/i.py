#coding=utf-8
'''
    被错误模板函数使用的内部对象是 RichTraceback. 该对象也可以被直接用于提供自定义错误视图。下面是一个范例应用，可以描述其一般使用的 API:
'''
from mako.lookup import TemplateLookup
from mako.exceptions import RichTraceback
try:
    mylookup=TemplateLookup(
        directories=['/home/workspace/gftop/MakoLearning/src/BasicUsage/docs'],
    )
    mytemplate=mylookup.get_template('mytmpl.txt')
    print mytemplate.render(
        name='高飞',
        sex='男',
        age=23,        
)
except:
    mytraceback=RichTraceback()
    for (filename,lineno,function,line) in mytraceback.traceback:
        print 'File %s,line %s,in %s'%(filename,lineno,function)
        print line,'\n'
    print '%s: %s'%(str(mytraceback.error.__class__.__name__),mytraceback.error)
