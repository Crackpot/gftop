from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1244629419.029047
_template_filename='/home/workspace/gftop/MakoLearning/src/Syntax/docs/mytmpl2.txt'
_template_uri='mytmpl2.txt'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        unicode = context.get('unicode', UNDEFINED)
        range = context.get('range', UNDEFINED)
        name = context.get('name', UNDEFINED)
        len = context.get('len', UNDEFINED)
        sex = context.get('sex', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\u63a7\u5236\u7ed3\u6784\n\n\n\u63a7\u5236\u7ed3\u6784\u6307\u7684\u662f\u63a7\u5236\u7a0b\u5e8f\u6d41\u7a0b\u7684\u90a3\u4e9b\u8bed\u6cd5 \u2014 \u6761\u4ef6\uff08\u5982 if/else\uff09\uff0c\u5faa\u73af\uff08\u5982 while \u548c for\uff09\uff0c\u4ee5\u53ca try/except \u4e4b\u7c7b\u3002\n\u5728 Mako \u4e2d\uff0c\u63a7\u5236\u7ed3\u6784\u7528 % \u540e\u9644\u52a0\u5e38\u89c4 Python \u63a7\u5236\u7ed3\u6784\u7684\u5199\u6cd5\uff0c\u5e76\u7528\u53e6\u4e00\u4e2a % \u8bed\u6cd5 "end<name>" \u7ed3\u675f\u8bed\u53e5\u5757\u3002\u5176\u4e2d "<name>" \u662f\u8be5\u8868\u8fbe\u5f0f\u7684\u5173\u952e\u5b57\uff1a\n\n\u7528\u6237\uff1a')
        # SOURCE LINE 8
        __M_writer(unicode(unicode(name)))
        __M_writer(u'\nname\u957f\u5ea6\uff1a')
        # SOURCE LINE 9
        __M_writer(unicode(len(name)))
        __M_writer(u'\nname\u8f6c\u6362\u6210unicode\u683c\u5f0f\u7684\u957f\u5ea6\uff1a')
        # SOURCE LINE 10
        __M_writer(unicode(len(unicode(name))))
        __M_writer(u'\n\u6027\u522b\uff1a')
        # SOURCE LINE 11
        __M_writer(unicode(unicode(sex)))
        __M_writer(u'\n\n')
        # SOURCE LINE 13
        if sex==u'\u7537':
            # SOURCE LINE 14
            __M_writer(u'\t\u5148\u751f\n')
            # SOURCE LINE 15
        elif sex=='\u5973':
            # SOURCE LINE 16
            __M_writer(u'\t\u5973\u58eb\n')
            # SOURCE LINE 17
        else:
            # SOURCE LINE 18
            __M_writer(u'\t\u6027\u522b\u9519\u8bef\n')
        # SOURCE LINE 20
        __M_writer(u'\n\n\uff05 \u53ef\u4ee5\u51fa\u73b0\u5728\u4e00\u884c\u91cc\u7684\u4efb\u4f55\u4f4d\u7f6e\uff0c\u53ea\u8981\u5176\u524d\u9762\u6ca1\u6709\u5176\u4ed6\u6587\u672c\uff1b\u7f29\u8fdb\u662f\u65e0\u6240\u8c13\u7684\u3002Python \u4e2d\u7684\u6240\u6709\u201c\u5192\u53f7\u201d\u8868\u8fbe\u5f0f\u5728\u8fd9\u91cc\u90fd\u5b8c\u5168\u652f\u6301\uff0c\u5305\u62ec if/elif/else, while, for \u751a\u81f3 def\uff0c\u5c3d\u7ba1 Mako \u6709\u5176\u5185\u5efa\u7684\u529f\u80fd\u66f4\u5f3a\u5927\u7684 def \u6807\u7b7e\u3002\n\n')
        # SOURCE LINE 24
        for a in ['one','two','three','four','five']:
            # SOURCE LINE 25
            if a[0]=='t':
                # SOURCE LINE 26
                __M_writer(u"it's two or three\n")
                # SOURCE LINE 27
            elif a[0]=='f':
                # SOURCE LINE 28
                __M_writer(u"it's four or five\n")
                # SOURCE LINE 29
            else:
                # SOURCE LINE 30
                __M_writer(u"it's one\n")
        # SOURCE LINE 33
        __M_writer(u'')
        # SOURCE LINE 38
        __M_writer(u'\n')
        # SOURCE LINE 40
        __M_writer(u'\u6362\u884c\u8fc7\u6ee4\u5668(Newline Filters)\n\u53cd\u659c\u7ebf ("\\") \u5b57\u7b26\u653e\u5728\u4efb\u610f\u4e00\u884c\u7684\u540e\u9762\uff0c\u4f1a\u5403\u6389\u4e00\u4e2a\u6362\u884c\u7b26\u3002\nhere is a line that goes onto ')
        # SOURCE LINE 43
        __M_writer(u'another line.\n\nPython \u8bed\u53e5\u5757\n\u4efb\u610f python \u8bed\u53e5\u5757\u90fd\u53ef\u4ee5\u7528 ')
        # SOURCE LINE 46
 

        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin()]))
        __M_writer(u' \u6807\u7b7e\u6765\u5b9a\u4e49\uff1a\nthis is a template\n')
        # SOURCE LINE 48

        x=[i*3 for i in range(0,9,2)]
        
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['i','x'] if __M_key in __M_locals_builtin()]))
        # SOURCE LINE 50
        __M_writer(u'\n')
        # SOURCE LINE 51
        for item in x:
            # SOURCE LINE 52
            __M_writer(unicode(item))
            __M_writer(u' ')
        # SOURCE LINE 54
        __M_writer(u'\n\u5728 <\uff05 \uff05> \u5185\u5b9a\u4e49\u7684 python \u4ee3\u7801\uff0c\u5176\u6574\u4f53\u7684\u7f29\u8fdb\u91cf\u662f\u4e0d\u91cd\u8981\u7684\uff0c\u4f46\u662f\u4ed6\u4eec\u5185\u90e8\u7684\u8bed\u53e5\u4e4b\u95f4\u5fc5\u987b\u6709\u6b63\u786e\u7684\u7f29\u8fdb\u5c42\u6b21\uff08\u56e0\u4e3a\u8fd9\u91cc\u6ca1\u6cd5\u4f7f\u7528 end\uff09\uff0cMako \u7684\u7f16\u8bd1\u5668\u4f1a\u8c03\u6574 python \u8bed\u53e5\u5757\u7684\u7f29\u8fdb\u5c42\u6b21\u4e0e\u5176\u5468\u56f4\u7684\u5176\u4ed6\u751f\u6210\u7684 Python \u4ee3\u7801\u76f8\u914d\u5408\u3002')
        return ''
    finally:
        context.caller_stack._pop_frame()


