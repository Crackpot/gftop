#coding=utf8
import settings
from django.conf.urls.defaults import *
from simplecms import views
from simplecms.search import views as sv
from simplecms.coltrane.feeds import CategoryFeed, LatestEntriesFeed 

from django.contrib import admin
admin.autodiscover()

feeds = {'entries': LatestEntriesFeed,
         'categories': CategoryFeed}

urlpatterns = patterns('',
    # Example:
    # (r'^simplecms/', include('simplecms.foo.urls')),
    
    (r'^feeds/(?P<url>.*)/$',
     'django.contrib.syndication.views.feed',
     { 'feed_dict': feeds }),
     
    (r'^$', views.index),
    (r'^search/$', sv.search),
    
    (r'^weblog/categories/', include('simplecms.coltrane.urls.categories')),
    (r'^weblog/links/', include('simplecms.coltrane.urls.links')),
    (r'^weblog/tags/', include('simplecms.coltrane.urls.tags')),
    (r'^weblog/', include('simplecms.coltrane.urls.entries')),
    
    (r'^snippets/', include('simplecms.cab.urls.snippets')),
    (r'^snippets/tags/', include('simplecms.cab.urls.tags')),
    (r'^snippets/languages/', include('simplecms.cab.urls.languages')),
    (r'^snippets/bookmarks/', include('simplecms.cab.urls.bookmarks')),
    (r'^popular/', include('simplecms.cab.urls.popular')),
    
    (r'^signup/', 'simplecms.views.signup'),

    (r'^comments/', include('django.contrib.comments.urls')),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT }),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT + '/css'}),
    # tiny_mce.js
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': settings.MEDIA_ROOT + '/javascripts/tinymce/jscripts/tiny_mce'}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # flatpages相关
    (r'', include('django.contrib.flatpages.urls')),
)
