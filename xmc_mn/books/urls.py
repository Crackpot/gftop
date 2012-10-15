from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    #(r'^latest/$', views.latest_books),
    (r'^$', views.latest_books),
    (r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    (r'^contact/$', views.contact),
)
