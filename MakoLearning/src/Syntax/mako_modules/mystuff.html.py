from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1244633172.5232589
_template_filename='/home/workspace/gftop/MakoLearning/src/Syntax/docs/mystuff.html'
_template_uri='mystuff.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = ['func']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_func(context):
    context.caller_stack._push_frame()
    try:
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\t\u8fd9\u662f\u4e00\u4e2a\u51fd\u6570\n')
        # SOURCE LINE 4
        for i in range(0,7,2):
            # SOURCE LINE 5
            __M_writer(u'\t\t')
            __M_writer(unicode(i))
            __M_writer(u'')
        return ''
    finally:
        context.caller_stack._pop_frame()


