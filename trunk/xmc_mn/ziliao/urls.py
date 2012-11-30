#coding=utf8
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from ziliao.models import Ziliao

urlpatterns = patterns('django.views.generic',
    url(r'^$', 'simple.direct_to_template',
        kwargs={
            'template':'ziliao/index.html',
            'extra_context':{'ziliao_list':lambda:Ziliao.objects.all()}
                },
        name = 'index'
        ),
)
