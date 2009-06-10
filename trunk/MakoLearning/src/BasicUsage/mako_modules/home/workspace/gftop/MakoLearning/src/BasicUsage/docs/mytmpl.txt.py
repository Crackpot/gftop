from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1244620768.430388
_template_filename='/home/workspace/gftop/MakoLearning/src/BasicUsage/docs/mytmpl.txt'
_template_uri='/home/workspace/gftop/MakoLearning/src/BasicUsage/docs/mytmpl.txt'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        age = context.get('age', UNDEFINED)
        name = context.get('name', UNDEFINED)
        sex = context.get('sex', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\u60a8\u597d,')
        __M_writer(unicode(name))
        __M_writer(u'\uff01\n\u6027\u522b\uff1a')
        # SOURCE LINE 3
        __M_writer(unicode(sex))
        __M_writer(u'\n\u5e74\u9f84\uff1a')
        # SOURCE LINE 4
        __M_writer(unicode(age))
        __M_writer(u'\n')
        # SOURCE LINE 5
        if sex=='\u7537':
            # SOURCE LINE 6
            __M_writer(u'\t\u5148\u751f\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


