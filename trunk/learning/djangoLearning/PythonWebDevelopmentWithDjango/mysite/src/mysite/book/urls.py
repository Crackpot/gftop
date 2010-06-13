#coding=utf8
from django.conf.urls.defaults import *
from mysite.book.views import book

urlpatterns = patterns('',
    url(r'^$',book),
)
