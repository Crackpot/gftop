from django.conf.urls.defaults import *
from views import JieyueListView, JieyueUpdateView, JieyueCreateView, \
    JieyueDeleteView, ZiliaoListView, ZiliaoUpdateView, ZiliaoCreateView, \
    ZiliaoDeleteView

urlpatterns = patterns('',
)

ziliao_patterns = patterns('',
    url(r'^list/page(?P<page>[0-9]+)/(\?.*)?$',
        ZiliaoListView.as_view(),
        name='list'),
    url(r'^update/(?P<pk>\d+)/$',
        ZiliaoUpdateView.as_view(),
        name='update'),
    url(r'^create/$',
        ZiliaoCreateView.as_view(),
        name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$',
        ZiliaoDeleteView.as_view(),
        name='delete'),
)

newpatterns = patterns('',
    url(r'^ziliao/', include(ziliao_patterns, namespace="ziliao")),
)

try:
    urlpatterns += newpatterns
except NameError:
    urlpatterns = newpatterns

jieyue_patterns = patterns('',
    url(r'^list/page(?P<page>[0-9]+)/(\?.*)?$',
        JieyueListView.as_view(),
        name='list'),
    url(r'^update/(?P<pk>\d+)/$',
        JieyueUpdateView.as_view(),
        name='update'),
    url(r'^create/$',
        JieyueCreateView.as_view(),
        name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$',
        JieyueDeleteView.as_view(),
        name='delete'),
)

newpatterns = patterns('',
    url(r'^jieyue/', include(jieyue_patterns, namespace="jieyue")),
)

try:
    urlpatterns += newpatterns
except NameError:
    urlpatterns = newpatterns
from django.conf.urls.defaults import *
from views import ZiliaoListView, ZiliaoUpdateView, ZiliaoCreateView, ZiliaoDeleteView

ziliao_patterns= patterns('',
    url(r'^list/page(?P<page>[0-9]+)/(\?.*)?$', 
        ZiliaoListView.as_view(),
        name='list'),
    url(r'^update/(?P<pk>\d+)/$', 
        ZiliaoUpdateView.as_view(),
        name='update'),
    url(r'^create/$', 
        ZiliaoCreateView.as_view(),
        name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', 
        ZiliaoDeleteView.as_view(),
        name='delete'),
)

newpatterns = patterns('',
    url(r'^ziliao/', include(ziliao_patterns, namespace="ziliao")),
)

try:
    urlpatterns+=newpatterns
except NameError:
    urlpatterns=newpatterns
