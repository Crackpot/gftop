#coding=utf8
from django.conf.urls.defaults import *
from simplecms.coltrane.models import Entry

# 和月份无关的通用视图不需要month_format
entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

# 和月份相关的通用视图需要month_format
entry_info_dict_with_month = {'month_format': '%m'}
entry_info_dict_with_month.update(entry_info_dict)

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$',
        'archive_index',
        entry_info_dict,
        'coltrane_entry_archive_index'), # coltrane/entry_archive.html

    (r'^(?P<year>\d{4})/$',
        'archive_year',
        entry_info_dict,
        'coltrane_entry_archive_year'), # coltrane/entry_archive_year.html

    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        'archive_month',
        entry_info_dict_with_month,
        'coltrane_entry_archive_month'), # coltrane/entry_archive_month.html

    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        'archive_day',
        entry_info_dict_with_month,
        'coltrane_entry_archive_day'), # coltrane/entry_archive_day.html

    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        'object_detail',
        entry_info_dict_with_month,
        'coltrane_entry_detail'), # coltrane/entry_detail.html
)
