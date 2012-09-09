#coding=utf8
from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from xmc_dj import settings

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'xmc_dj.views.home', name='home'),
    # url(r'^xmc_dj/', include('xmc_dj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    #(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()
