#coding=utf8
from django.conf.urls.defaults import *
from simplecms.coltrane import views
from django.views.generic.date_based import object_detail
from simplecms.coltrane.models import Entry

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}


urlpatterns = patterns('django.views.generic.date_based',
    (r'^/$',
        'archive_index',
        entry_info_dict,
        'coltrane_entry_archive_index'), # coltrane/entry_archive.html

    (r'^/(?P<year>\d{4})/$',
        'archive_year',
        entry_info_dict,
        'coltrane_entry_archive_year'), # coltrane/entry_archive_year.html

    (r'^/(?P<year>\d{4})/(?P<month>\d{2})/$',
        'archive_month',
        entry_info_dict,
        'coltrane_entry_archive_month'), # coltrane/entry_archive_month.html

    (r'^/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        'archive_day',
        entry_info_dict,
        'coltrane_entry_archive_day'), # coltrane/entry_archive_day.html

    (r'^/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        'object_detail',
        entry_info_dict,
        'coltrane_entry_detail'), # coltrane/entry_detail.html
)
