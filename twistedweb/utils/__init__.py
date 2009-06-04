#coding=utf-8
import sys
sys.path.append('/home/workspace/gftop/twistedweb')
import settings
from mako.template import Template
from mako.lookup import TemplateLookup
from mako.exceptions import TopLevelLookupException

lookup = TemplateLookup(\
    directories=[ settings.MAKO_TEMPLATE_DIRS ],\
    default_filters=['decode.utf_8'],\
    output_encoding='utf-8', \
    encoding_errors='replace',\
    filesystem_checks=False,
)

def get_template(template_name):
    return lookup.get_template(template_name)
    
def render_to_response(template_name, **kwargs):
    template = get_template(template_name)
    return template.render(**kwargs)