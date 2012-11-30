#coding=utf8
from django.conf.urls.defaults import *
from django.contrib import admin
from products.models import Catalog, Product


admin.autodiscover()

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list', {'queryset': Product.objects.all()},
        name='product_list'),
                       
    url(r'^product/(?P<slug>[-\w]+)/$', 'object_detail',
        {'queryset': Product.objects.all()},
        name='product_detail')
)