#coding=utf8
from django.conf.urls.defaults import *
from mysite.polls import views
from mysite.polls.models import Poll
from django.views.generic import list_detail

info_dict = {
    'queryset': Poll.objects.all()
}

urlpatterns = patterns('',
    #(r'^$', views.index), # 原始
    #(r'^(?P<poll_id>\d+)/$', views.detail), # 原始
    #(r'^(?P<poll_id>\d+)/results/$', views.results), # 原始
    (r'^$', list_detail.object_list, info_dict), # 通用视图
    (r'^(?P<object_id>\d+)/$', list_detail.object_detail, info_dict), # 通用视图
    url(r'^(?P<object_id>\d+)/results/$', list_detail.object_detail, dict(info_dict, template_name='polls/results.html'), 'poll_results'),
    (r'^(?P<poll_id>\d+)/vote/$', views.vote), # 原始
)
