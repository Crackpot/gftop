#coding=utf-8
'''
    处理异常
    模板异常可能在两种截然不同的地方出现。第一种是当你查找，分析和编译模板时，另一种是当你运行模板的时候。
在模板的运行过程中，异常通常从产生问题的 python 代码出抛出。Mako 有其独立的一套异常类，它们大多数针对模板构造过程的查找和词法分析/编译阶段。Mako 还提供了一些库函数，这些函数用来帮助提供 Mako 相关的异常栈跟踪信息，并可用纯文本或 HTML 方式格式化异常信息。不管是哪种情况，这些处理函数的作用在于将 Python 文件名，行号，以及代码例子转换为 Mako 的模板文件名，行号，以及代码范例。在跟踪栈里对应于某个 Moko 模板的每一行，都回被转换为和源模板文件相关的。
    为了格式化异常跟踪信息，系统提供了 text_error_template 和 html_error_template 函数。它们都利用了 sys.exc_info() 函数来获取最近抛出的异常信息。下面是常见的用法：
'''
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
try:
    mylookup=TemplateLookup(
        directories=['/home/workspace/gftop/MakoLearning/src/BasicUsage/docs'],
        output_encoding='utf-8',
        encoding_errors='replace',
    )
    mytemplate=mylookup.get_template('mytmpl.txt')
    '''HTML 输出函数也内建到了 Template 中。通过 format_exceptions 这个标志位参数。这样，任何在 template 的 render 阶段引发的异常，都会使得 template 的输出内容被 html_error_template 方法的输出所替代。 '''
#    mytemplate=Template(
#        filename='/home/workspace/gftop/MakoLearning/src/BasicUsage/docs/mytmpl.txt',
#        format_exceptions=True,
#    )
    print mytemplate.render(
        name=u'高飞',
        sex=u'男',
        age=23,
    )
except:
    #print exceptions.text_error_template().render()
    print exceptions.html_error_template().render()     #使用HTML的输出函数
'''
    上述模板的编译阶段发生在你构造 Template 对象本身的时候，并且没有定义输出流。所以，在查找/解析/编译阶段引发的异常不会被处理，而是像平常那样被继续抛出到更高层次的调用堆栈上（繁殖, propagate）。虽然 pre-render traceback 不会包含任何 Mako 特定的行，这意味着发生在 rendering 之前的异常，以及 rendering 过程中发生的异常，需要用不同的办法分别处理。因此，上面的 try/except 模式可能是比较通用的一种写法。
'''