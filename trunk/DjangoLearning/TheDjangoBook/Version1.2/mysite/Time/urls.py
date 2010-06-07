#coding=utf8
from django.conf.urls.defaults import *
from mysite.Time import  views 
urlpatterns = patterns('',
    (r'^$', views.current_datetime),
    (r'^plus/(\d{1,2})/$', views.hours_ahead),
)
