#coding=utf8
from django.conf.urls.defaults import *
from simplecms.coltrane.models import Link

link_info_dict = {
    'queryset': Link.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('',
    (r'^/$',
     'archive_index',
     link_info_dict,
     'coltrane_link_archive_index')
)
