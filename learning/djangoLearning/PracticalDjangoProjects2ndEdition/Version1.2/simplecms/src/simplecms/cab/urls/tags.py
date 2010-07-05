#coding=utf8
from django.conf.urls.defaults import *;
from simplecms.cab.models import Snippet
from tagging.models import Tag

urlpatterns = patterns('',
    (r'^(?P<tag>[-\w]+)/$',
     'tagging.views.tagged_object_list',
     {'queryset_or_model': Snippet,
      'template_name': 'cab/snippets_by_tag.html'}),
)