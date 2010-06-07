#coding=utf8
from django.conf.urls.defaults import *
from mysite.contact import  views 
urlpatterns = patterns('',
    (r'^$', views.contact), # 使用django.forms
    (r'^thanks/$', views.thanks),
    (r'^original/$', views.contact_original), # 自己编写表单
)
