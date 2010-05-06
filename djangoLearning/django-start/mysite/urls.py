from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

from mysite.settings import MEDIA_ROOT
from mysite.maintenance.meta import sitemaps

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'home.html'}),
    (r'^items/', include('mysite.items.urls')),

    (r'^comments/post/', 'mysite.comm.views.redirect_post_comment'),
    (r'^comments/', include('django.contrib.comments.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),

    (r'^accounts/', include('mysite.accounts.urls')),
    url(r'^captcha/', include('captcha.urls')),
    #(r'^profiles/', include('profiles.urls')),

    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^robots.txt$', include('robots.urls')),

    # Site Media: development handler, in release mode the media files should be handled directly by Apache
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)
