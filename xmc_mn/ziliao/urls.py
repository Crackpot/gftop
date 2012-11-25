#coding=utf8
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from ziliao.models import Ziliao

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Ziliao.objects.order_by('-zl_cundangshijian')[:5],
            context_object_name='latest_ziliao_list',
            template_name='ziliao/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Ziliao,
            template_name='ziliao/detail.html')),
#    url(r'^(?P<pk>\d+)/results/$',
#        DetailView.as_view(
#            model=Ziliao,
#            template_name='ziliao/results.html'),
#        name='Ziliao_results'),
#    url(r'^(?P<Ziliao_id>\d+)/vote/$', 'Ziliaos.views.vote'),
)