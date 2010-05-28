#coding=utf8
from django.conf.urls.defaults import *
from mysite.books import views
urlpatterns = patterns('',
    (r'^search$', views.search),
)
