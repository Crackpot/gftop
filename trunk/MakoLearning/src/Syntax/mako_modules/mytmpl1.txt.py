from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1244621942.4186931
_template_filename='/home/workspace/gftop/MakoLearning/src/Syntax/docs/mytmpl1.txt'
_template_uri='mytmpl1.txt'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        y = context.get('y', UNDEFINED)
        x = context.get('x', UNDEFINED)
        pow = context.get('pow', UNDEFINED)
        max = context.get('max', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\u6700\u7b80\u5355\u7684\u8868\u8fbe\u5f0f\u662f\u53d8\u91cf\u66ff\u6362\u3002\u5176\u8bed\u6cd5\u662f "$\uff5b\uff5d"\uff0c\u53d7 Perl, Genshi, JSP EL \u548c\u5176\u4ed6\u4e00\u4e9b\u8bed\u8a00\u7684\u542f\u53d1\uff1a\n\u53d8\u91cfx=')
        # SOURCE LINE 2
        __M_writer(unicode(x))
        __M_writer(u'\n\u53d8\u91cfy=')
        # SOURCE LINE 3
        __M_writer(unicode(y))
        __M_writer(u'\n\u4ee5\u4e0a\u4ee3\u7801\u4e2d\uff0cx \u7684\u5b57\u7b26\u4e32\u8868\u793a\u5f62\u5f0f\u5c06\u88ab\u5e94\u7528\u5230\u6a21\u677f\u7684\u8f93\u51fa\u6d41\u4e2d\u3002x \u7684\u503c\u901a\u5e38\u6765\u6e90\u4e8e\u4f60\u63d0\u4f9b\u7ed9\u6a21\u677f rendering \u51fd\u6570\u4f5c\u4e3a\u53c2\u6570\u7684 Context \u53d8\u91cf\u3002\u5982\u679c x \u7684\u503c\u672a\u6307\u5b9a\u7ed9\u6a21\u677f\uff0c\u5e76\u4e14\u4e5f\u672a\u6307\u5b9a\u4e3a\u5c40\u90e8\u53d8\u91cf\uff0c\u5219\u4f1a\u4f30\u7b97\u4e3a\u4e00\u4e2a\u7279\u6b8a\u7684\u503c UNDEFINED. \n$\uff5b\uff5d \u4e2d\u7684\u5185\u5bb9\u4f1a\u88ab Python \u76f4\u63a5\u4f30\u7b97\uff0c\u6240\u4ee5\u5404\u79cd\u8868\u8fbe\u5f0f\u90fd\u662f\u652f\u6301\u7684\uff1a\n\u8f83\u5927\u7684\u6570\u5b57\u4e3a\uff1a')
        # SOURCE LINE 6
        __M_writer(unicode(max(x,y)))
        __M_writer(u'\npythagorean theorem:  ')
        # SOURCE LINE 7
        __M_writer(unicode(pow(x,2) + pow(y,2)))
        __M_writer(u'\n\nMako \u5305\u542b\u4e86\u4e00\u7cfb\u5217\u5185\u5efa\u7684\u8f6c\u4e49\u673a\u5236\uff0c\u5305\u62ec HTML, URI \u548c XML \u8f6c\u4e49\uff0c\u4ee5\u53ca "trim" \u51fd\u6570\u3002\u8f6c\u4e49\u7684\u52a8\u4f5c\u53ef\u4ee5\u901a\u8fc7 | \u8fd0\u7b97\u7b26\u9644\u52a0\u5230\u8868\u8fbe\u5f0f\u540e\u9762\uff1a\n\n')
        # SOURCE LINE 11
        __M_writer(filters.url_escape(unicode("This is some text")))
        __M_writer(u'\n\n\u4e0a\u4f8b\u4e2d\u5bf9\u8868\u8fbe\u5f0f\u8fdb\u884c\u4e86 URL \u8f6c\u4e49\uff0c\u5176\u7ed3\u679c\u662f\uff1athis+is+some+text. \u5176\u4e2d u \u4ee3\u8868 URL \u8f6c\u4e49\uff0c\u4e0e\u4e4b\u7c7b\u4f3c\u7684\uff0ch \u4ee3\u8868 HTML \u8f6c\u4e49\uff0cx \u4ee3\u8868 XML \u8f6c\u4e49\uff0c\u800c trim \u5219\u662f\u901a\u5e38\u7684 trim \u51fd\u6570\u3002\n\u53ef\u4ee5\u5728 Filtering and Buffering \u4e2d\u83b7\u53d6\u66f4\u591a\u5173\u4e8e\u8fc7\u6ee4\u5668\u51fd\u6570\u7684\u5185\u5bb9\uff0c\u5305\u62ec\u5982\u4f55\u521b\u5efa\u4f60\u81ea\u5df1\u7684\u8fc7\u6ee4\u5668\u3002\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


