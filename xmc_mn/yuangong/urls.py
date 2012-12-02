#coding=utf8
from django.conf.urls import patterns
import views

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^output/$', views.output),
    (r'^upload/$', views.upload),
)
