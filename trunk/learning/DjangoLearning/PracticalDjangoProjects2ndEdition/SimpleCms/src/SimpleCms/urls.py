# coding=utf8
import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^search$','SimpleCms.search.views.search'), # 去掉斜杠，直接为query?q=foo
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT + '/javascripts/tinymce/jscripts/tiny_mce'}),
    (r'^weblog/categories/', include('coltrane.urls.categories')),
    (r'^weblog/links/', include('coltrane.urls.links')),
    (r'^weblog/tags/', include('coltrane.urls.tags')),
    (r'^weblog/', include('coltrane.urls.entries')),
    (r'^$','SimpleCms.views.index'),
    (r'', include('django.contrib.flatpages.urls')),
)
