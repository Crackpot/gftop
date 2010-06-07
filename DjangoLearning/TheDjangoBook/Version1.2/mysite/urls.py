#coding=utf8
from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from mysite import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),
    
    (r'^$', views.index), #没有反斜杠
    (r'^display_meta/$', views.display_meta),
    (r'^hello/$', views.hello),
    (r'^add/$', views.add),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    # 其他应用
    (r'contact/', include('mysite.contact.urls')),
    (r'^books/', include('mysite.books.urls')),
    (r'^time/', include('mysite.Time.urls')),
    (r'^polls/', include('mysite.polls.urls')),
    (r'^accounts/', include('registration.urls')),
    (r'^cms/', include('cms.urls')),
)

urlpatterns += patterns('',
    # 使用通用视图
    (r'^about/$', direct_to_template, {'template':'about/index.html'}),
    (r'^about/(\w+)/$', views.about_pages),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^debug/$', views.debug)
    )
