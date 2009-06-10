from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1244631308.550756
_template_filename='/home/workspace/gftop/MakoLearning/src/Syntax/docs/mytmpl3.html'
_template_uri='mytmpl3.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['account', 'hello']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        username = context.get('username', UNDEFINED)
        def account():
            return render_account(context.locals_(__M_locals))
        def hello():
            return render_hello(context.locals_(__M_locals))
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
        __M_writer(u'\n\n')
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
        __M_writer(u':\n\t')
        # SOURCE LINE 13

        accountdata={1:1,2:2,}
                
        
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


