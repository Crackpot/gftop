#coding=utf8
from django.conf.urls.defaults import *

from simplecms.coltrane.models import Category

urlpatterns = patterns('',
    (r'^/$',
     'django.views.generic.list_detail.object_list',
     {'queryset': Category.objects.all()},
     ),
     
    (r'^/(?P<slug>[-\w]+)/$',
     'simplecms.coltrane.views.category_detail'),
)