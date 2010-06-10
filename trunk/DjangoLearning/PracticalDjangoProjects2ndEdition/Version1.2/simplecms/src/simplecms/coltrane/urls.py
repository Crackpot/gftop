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
    #(r'^/$', views.entries_index),
    (r'^/$',
        'django.views.generic.date_based.archive_index',
        entry_info_dict), # coltrane/entry_archive.html
    (r'^/(?P<year>\d{4})/$',
        'django.views.generic.date_based.archive_year',
        entry_info_dict), # coltrane/entry_archive_year.html
    (r'^/(?P<year>\d{4})/(?P<month>\w{3})/$',
        'django.views.generic.date_based.archive_month',
        entry_info_dict), # coltrane/entry_archive_month.html
    (r'^/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
        'django.views.generic.date_based.archive_day',
        entry_info_dict), # coltrane/entry_archive_day.html
    (r'^/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        'django.views.generic.date_based.object_detail',
        entry_info_dict), # coltrane/entry_detail.html
)
