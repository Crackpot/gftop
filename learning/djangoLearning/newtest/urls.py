from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^newtest/', include('newtest.foo.urls')),
    (r'^$', 'newtest.helloworld.index'),
    (r'^add/$', 'newtest.add.index'),
    (r'^list/$', 'newtest.list.index'),
    (r'^csv/(?P<filename>\w+)/$', 'newtest.csv_test.output'),
    (r'^login/$', 'newtest.login.login'),
    (r'^logout/$', 'newtest.login.logout'),
    (r'^wiki/$','newtest.wiki.views.index'),
    (r'^wiki/(?P<pagename>\w+)/$','newtest.wiki.views.index'),
    (r'^wiki/(?P<pagename>\w+)/edit/$','newtest.wiki.views.edit'),
    (r'^wiki/(?P<pagename>\w+)/save/$','newtest.wiki.views.save'),
    


    
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
