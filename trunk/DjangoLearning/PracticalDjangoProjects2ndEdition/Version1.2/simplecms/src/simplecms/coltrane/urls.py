#coding=utf8
from django.conf.urls.defaults import *
from simplecms.coltrane import views
urlpatterns = patterns('',
    (r'^/$', views.entries_index),
    #(P?<slug>[-\w]+)/$
    (r'^/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>\w+)/$', views.entry_detail),
    (r'^/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(P?<slug>[-\w]+)/$', views.entries_index),
)