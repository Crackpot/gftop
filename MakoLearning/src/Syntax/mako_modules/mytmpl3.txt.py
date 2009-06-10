from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1244633171.706691
_template_filename='/home/workspace/gftop/MakoLearning/src/Syntax/docs/mytmpl3.txt'
_template_uri='mytmpl3.txt'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['account', 'hello', 'account1']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 35
    ns = runtime.Namespace('mystuff', context._clean_inheritance_tokens(), templateuri='mystuff.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, 'mystuff')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        username = context.get('username', UNDEFINED)
        def account():
            return render_account(context.locals_(__M_locals))
        mystuff = _mako_get_namespace(context, 'mystuff')
        def hello():
            return render_hello(context.locals_(__M_locals))
        def account1(accountname,type='regular'):
            return render_account1(context.locals_(__M_locals),accountname,type)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'')
        # SOURCE LINE 5
        __M_writer(u'')
        # SOURCE LINE 6
        __M_writer(u'the def: ')
        __M_writer(unicode(hello()))
        __M_writer(u'\n\u5982\u679c <\uff05def> \u6ca1\u6709\u5d4c\u5957\u5b9a\u4e49\u5728\u53e6\u4e00\u4e2a <\uff05def> \u4e2d\uff0c\u5219\u79f0\u4e3a\u9876\u5c42\u7684 def, \u5b83\u53ef\u4ee5\u5728\u6a21\u677f\u7684\u4efb\u4f55\u5730\u65b9\u88ab\u4f7f\u7528\uff0c\u751a\u81f3\u53ef\u4ee5\u5728\u5b9a\u4e49\u5b83\u7684\u4f4d\u7f6e\u4e4b\u524d\u3002\n\u6240\u6709\u7684 defs, \u4e0d\u7ba1\u662f\u4e0d\u662f\u9876\u5c42\u7684\uff0c\u90fd\u53ef\u4ee5\u8bbf\u95ee\u5f53\u524d\u7684\u4e0a\u4e0b\u6587\u540d\u79f0\u7a7a\u95f4\uff0c\u548c\u6a21\u677f\u7684\u8bbf\u95ee\u6743\u9650\u5b8c\u5168\u4e00\u6837\u3002\u8bbe\u60f3\u4e0b\u5217\u6a21\u677f\u5728\u6267\u884c\u65f6\u88ab\u6307\u5b9a\u4e86\u4e00\u4e2a\u5305\u542b username \u548c accountdata \u53d8\u91cf\u7684\u4e0a\u4e0b\u6587\uff1a\nHello ')
        # SOURCE LINE 9
        __M_writer(unicode(username))
        __M_writer(u',how are you? Lets see what your account says:')
        # SOURCE LINE 10
        __M_writer(unicode(account()))
        __M_writer(u'')
        # SOURCE LINE 19
        __M_writer(u'')
        # SOURCE LINE 20
        __M_writer(u'username \u548c accountdata \u4e24\u4e2a\u53d8\u91cf\u5c06\u4f1a\u663e\u793a\u5728\u4e3b\u6a21\u677f\u7684 body \u4e2d\uff0c\u540c\u6837\u4e5f\u4f1a\u663e\u793a\u5728 account() def \u7684 body \u4e2d\u3002\n\n\u65e2\u7136 defs \u4e0d\u8fc7\u5c31\u662f python \u51fd\u6570\uff0c\u4f60\u81ea\u7136\u4e5f\u80fd\u591f\u5b9a\u4e49\u548c\u4f20\u9012\u53c2\u6570\u4e86:\n')
        # SOURCE LINE 23
        __M_writer(unicode(account1(accountname='crackpot')))
        __M_writer(u'')
        # SOURCE LINE 26
        __M_writer(u'\n\u5f53\u4f60\u4e3a def \u5b9a\u4e49\u53c2\u6570\u65f6\uff0c\u4ed6\u4eec\u9700\u8981\u9075\u4ece Python \u7684\u89c4\u5b9a\uff08\u6bd4\u5982\uff0c\u9664\u4e86\u63d0\u4f9b\u4e86\u9ed8\u8ba4\u503c\u7684\u5173\u952e\u5b57\u53c2\u6570\u4e4b\u5916\u7684\u6240\u6709\u53c2\u6570\uff0c\u90fd\u9700\u8981\u63d0\u4f9b\uff09\u3002\u8fd9\u548c\u4e0a\u4e0b\u6587\u5c42\u6b21\u7684\u53d8\u91cf\u4e0d\u540c\uff0c\u540e\u8005\u5bf9\u4e0d\u5b58\u5728\u7684\u540d\u79f0\u4f1a\u4f30\u7b97\u4e3a UNDEFINED \u800c\u4e0d\u662f\u51fa\u9519\u3002\n\u4ece\u5176\u4ed6\u6587\u4ef6\u8c03\u7528 defs\n\n\u9876\u5c42\u7684 <\uff05defs> \u88ab\u7f16\u8bd1\u5230\u6a21\u677f\u5bf9\u5e94\u7684\u6a21\u5757\u4e2d\uff0c\u5e76\u4e14\u53ef\u4ee5\u88ab\u4ece\u5916\u90e8\u8c03\u7528\uff1b\u5305\u62ec\u4ece\u5176\u4ed6\u6a21\u677f\uff0c\u6216\u662f\u666e\u901a\u7684 Python \u4ee3\u7801\u6765\u8c03\u7528\u3002\u4ece\u5176\u4ed6\u6a21\u677f\u4e2d\u8c03\u7528 <\uff05def> \u6709\u70b9\u50cf\u4f7f\u7528 <\uff05include> \u2014\u2014 \u5dee\u522b\u5728\u4e8e\uff0c\u4f60\u662f\u5728\u8c03\u7528\u6a21\u677f\u4e2d\u7684\u4e00\u4e2a\u51fd\u6570\uff0c\u800c\u4e0d\u662f\u6574\u4e2a\u6a21\u677f\u3002\n\n\u8fdc\u7a0b\u7684 <\uff05def> \u8c03\u7528\u4e5f\u6709\u70b9\u7c7b\u4f3c\u4e8e Python \u4e2d\u8c03\u7528\u53e6\u4e00\u4e2a\u6a21\u5757\u4e2d\u7684\u51fd\u6570\u7684\u60c5\u5f62\u3002\u9700\u8981\u6709\u4e00\u4e2a\u201c\u5bfc\u5165\u201d\u7684\u6b65\u9aa4\uff0c\u4ee5\u4fbf\u4ece\u5176\u4ed6\u6a21\u677f\u4e2d\u8403\u53d6\u51fa\u540d\u79f0\uff0c\u6dfb\u52a0\u5230\u4f60\u81ea\u5df1\u7684\u6a21\u677f\u4e2d\uff1b\u7136\u540e\u8fd9\u4e9b\u540d\u79f0\u7684\u51fd\u6570\u624d\u53ef\u4ee5\u88ab\u8c03\u7528\u3002\n\n\u8981\u5bfc\u5165\u53e6\u4e00\u4e2a\u6a21\u677f\uff0c\u4f7f\u7528 <\uff05namespace> \u6807\u7b7e:\n')
        # SOURCE LINE 35
        __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(unicode(mystuff.func()))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_account(context):
    context.caller_stack._push_frame()
    try:
        username = context.get('username', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n\tAccount for ')
        # SOURCE LINE 12
        __M_writer(unicode(username))
        __M_writer(u':')
        # SOURCE LINE 13
        __M_writer(u'\t')

        accountdata={'1':'one','2':'two',}
                
        
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 16
        for row in accountdata:
            # SOURCE LINE 17
            __M_writer(u'\t\tValue:')
            __M_writer(unicode(row))
            __M_writer(u'<br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hello(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\nhelloworld\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_account1(context,accountname,type='regular'):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'')
        # SOURCE LINE 25
        __M_writer(u'\taccount name:')
        __M_writer(unicode(accountname))
        __M_writer(u',type ')
        __M_writer(unicode(type))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


