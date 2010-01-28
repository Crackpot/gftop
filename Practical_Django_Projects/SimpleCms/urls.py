# coding=utf8

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# 引入并自动发现admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^SimpleCms/', include('SimpleCms.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^search/$', 'SimpleCms.search.views.search'),
    # flatpages页面
    (r'', include('django.contrib.flatpages.urls')),
    # tiny_mce插件
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': './javascript/tiny_mce' },
        ),
)
