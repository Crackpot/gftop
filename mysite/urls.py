from django.conf.urls.defaults import *
from django.conf import settings
#from mysite.views import hello,current_datetime, hours_ahead,index,checkbrowser,display_meta

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mysite.views',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),
    (r'^$','index'),
    (r'^hello/$','hello'),
    (r'^time/$','current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    (r'^checkbrowser/$','checkbrowser'),
    (r'^displaymeta/$','display_meta'),
    (r'^(foo)/$','foo_view'),
    (r'^(bar)/$','bar_view'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/(.*)', admin.site.root),
)
urlpatterns+=patterns('mysite.books.views',
    (r'^search/$','search'),
    (r'^search_form/$','search_form'),
    (r'^contact/$','contact'),
    (r'^contact_form/$','contact_form'),
)