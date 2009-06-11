#coding=utf-8
'''
    Mako 模板是从文本流中进行解析的，流中可以包含任意内容: XML, HTML, email 文本，等等。模板中可以包含 Mako 特定的指令(directives)，可用于表示变量或表达式替换，控制结构（如条件和循环），服务器端注释，整段的 Python 代码，以及各种用于提供附加功能的标签(tags)。所有这些将被编译为真实的 Python 代码。这意味着你可以在 Mako 模板中利用 Python 几乎所有的强大特性。
'''
from mako.template import Template
from mako.lookup import TemplateLookup
mylookup=TemplateLookup(
    directories=['/home/workspace/gftop/MakoLearning/src/Namespaces/docs'],
    module_directory='/home/workspace/gftop/MakoLearning/src/Namespaces/mako_modules',
    output_encoding='utf-8',
    encoding_errors='replace',
    collection_size=500,
    filesystem_checks=True,
)
def server_template(templatename,**kwargs):
    mytemplate=mylookup.get_template(templatename)
    print mytemplate.render_unicode(**kwargs)
#server_template('components.html')
#server_template('index.html')
server_template('mytmpl1.txt')
