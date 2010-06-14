#coding=utf8
from django.conf.urls.defaults import *
from simplecms.coltrane.models import Entry, Link
from tagging.models import Tag

urlpatterns = patterns('',
    (r'^$',
     'django.views.generic.list_detail.object_list',
     {'queryset': Tag.objects.all()}),
     
    (r'^entries/(?P<tag>[-\w]+)/$',
     'tagging.views.tagged_object_list',
     {'queryset_or_model': Entry,
      # 默认将渲染coltrane/entry_list.html
      'template_name': 'coltrane/entries_by_tag.html'}),
      
    (r'^links/(?P<tag>[-\w]+)/$',
     'tagging.views.tagged_object_list',
     { 'queryset_or_model': Link,
      # 默认将渲染coltrane/link_list.html
      'template_name': 'coltrane/links_by_tag.html' }),
)
