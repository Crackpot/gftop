from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll
import views

urlpatterns = patterns('',
    url(r'^$', 'home.views.index'),
)