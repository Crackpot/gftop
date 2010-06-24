#coding=utf8
from django import template
from django.db.models import get_model

#from simplecms.coltrane.models import Entry

"""
# 原先写的简单标签
def do_latest_entries(parser, token):
    return LatestEntriesNode()

class LatestEntriesNode(template.Node):
    def render(self, context):
        context['latest_entries'] = Entry.live.all()[:5]
        return ''
"""
    
# 更灵活的标签
def do_latest_content(parser, token):
    #bits = token.contents.split()
    bits = token.split_contents() # 切割开来
    if len(bits) != 5:
        raise template.TemplateSyntaxError("'get_latest_content' tag takes exactly four arguments")
    model_args = bits[1].split('.')
    
    if len(model_args) != 2:
        raise template.TemplateSyntaxError("First argument to 'get_latest_content' must be an 'application name'.'model name' string")
    model = get_model(*model_args)
    # 看看传递过来的参数包含什么内容
    print 'parser => %s\n token => %s\n bits => %s\n model_args => %s\n model => %s\n' %(parser, token, bits, model_args, model)
    if model is None:
        raise template.TemplateSyntaxError("'get_latest_content' tag got an invalid model: %s" % bits[1])
    return LatestContentNode(model, bits[2], bits[4])

class LatestContentNode(template.Node):
    def __init__(self, model, num, varname):
        self.model = model
        self.num = int(num)
        self.varname = varname
        
    def render(self, context):
        #context[self.varname] =  self.model.objects.all()[:self.num]
        context[self.varname] =  self.model._default_manager.all()[:self.num]
        return ''
    
register = template.Library()
# register.tag('get_latest_entries', do_latest_entries)
register.tag('get_latest_content', do_latest_content)
