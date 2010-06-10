#coding=utf8
from django.conf.urls.defaults import *
from simplecms.coltrane import views
from django.views.generic.date_based import object_detail
from simplecms.coltrane.models import Entry

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}


urlpatterns = patterns('',
    (r'^/$', 'django.views.generic.date_based.archive_index',entry_info_dict),

    (r'^/$', views.entries_index),
    (r'^/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','django.views.generic.date_based.object_detail', entry_info_dict),

    (r'^/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', object_detail, entry_info_dict),
    (r'^/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.entry_detail),
)