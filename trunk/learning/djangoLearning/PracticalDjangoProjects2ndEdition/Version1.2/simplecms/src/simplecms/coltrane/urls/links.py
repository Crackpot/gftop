#coding=utf8
from django.conf.urls.defaults import *
from simplecms.coltrane.models import Link

link_info_dict = {
    'queryset': Link.objects.all(),
    'date_field': 'pub_date',
}

link_info_dict_with_month = {'month_format': '%m'}
link_info_dict_with_month.update(link_info_dict)

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$',
        'archive_index',
        link_info_dict,
        'coltrane_link_archive_index'), # coltrane/link_archive.html

    (r'^(?P<year>\d{4})/$',
        'archive_year',
        link_info_dict,
        'coltrane_link_archive_year'), # coltrane/link_archive_year.html

    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        'archive_month',
        link_info_dict_with_month,
        'coltrane_link_archive_month'), # coltrane/link_archive_month.html

    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        'archive_day',
        link_info_dict_with_month,
        'coltrane_link_archive_day'), # coltrane/link_archive_day.html

    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        'object_detail',
        link_info_dict_with_month,
        'coltrane_link_detail'), # coltrane/link_detail.html
)
