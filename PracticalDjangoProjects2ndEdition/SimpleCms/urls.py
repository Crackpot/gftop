# coding=utf8
import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
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
    (r'^search$','SimpleCms.search.views.search'), # 去掉斜杠，直接为query?q=foo
    (r'^$','SimpleCms.views.index'),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root':
            settings.MEDIA_ROOT + '/javascripts/tinymce/jscripts/tiny_mce'}),

    (r'^weblog/$', 'coltrane.views.entries_index'),
    (r'', include('django.contrib.flatpages.urls')),
)
