#coding=utf8
import settings
from django.conf.urls.defaults import *
from simplecms import views
from simplecms.search import views as sv

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^simplecms/', include('simplecms.foo.urls')),
    (r'^$',views.index ),
    (r'^search/$',sv.search ),
    (r'^weblog', include('simplecms.coltrane.urls')),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT }),
    # tiny_mce.js
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT + '/javascripts/tinymce/jscripts/tiny_mce'}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # flatpages相关
    #(r'', include('django.contrib.flatpages.urls')),
)
