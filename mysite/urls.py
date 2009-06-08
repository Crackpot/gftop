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
    (r'^time/now_in_london/$','now_in_london'),
    (r'^time/plus/(-?\d{1,2})/$', 'hours_ahead'),
    (r'^checkbrowser/$','checkbrowser'),
    (r'^displaymeta/$','display_meta'),
    (r'^foo/$','foo_view'),
    (r'^bar/$','bar_view'),
    (r'^say_hello/([\w\W]*)/$','say_hello'),
    (r'^say_goodbye/([\w\W]*)/$','say_goodbye'),
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
from django.views.generic.simple import direct_to_template
from mysite.books.views import about_pages
urlpatterns += patterns('',
    ('^about/$', direct_to_template, {
        'template': 'about.html'
    }),
    ('^about/(w+)/$',about_pages),
)

from django.views.generic import list_detail
from mysite.books.models import Publisher
from mysite.books.models import Book
def get_books():
    return Book.objects.all()
publisher_info = {
    "queryset" : Publisher.objects.all(),
    "template_object_name" : "publisher",
    "extra_context":{"book_list":get_books},
    "extra_context":{"book_list":Book.objects.all}
    #"extra_context":{"book_list":Book.objects.all()},
}
urlpatterns += patterns('',
    (r'^publishers/$', list_detail.object_list, publisher_info),
)

book_info={
    "queryset":Book.objects.all().order_by("-publication_date"),
    "template_object_name":"book",
}
urlpatterns+=patterns('',
    (r'^books/$',list_detail.object_list,book_info)
)
from mysite.books.models import Author
author_info={
    "queryset":Author.objects.all(),
    "template_object_name":"author",
}
urlpatterns+=patterns('',
    (r'^authors/$',list_detail.object_list,author_info)
)
OReilly_books={
    "queryset":Book.objects.filter(publisher__name="O'Reilly"),
    "template_object_name":"book",
    "template_name":"books/OReilly_list.html",
}
urlpatterns+=patterns('',
    (r'^books/OReilly/$',list_detail.object_list,OReilly_books),
)

urlpatterns+=patterns('mysite.books.views',
    (r'^books/(\w+)/$','books_by_publisher'),                      
)
from mysite.books.views import author_detail
urlpatterns+=patterns('',
    (r'^authors/(?P<author_id>d+)/$', author_detail),
)
urlpatterns+=patterns('mysite.books.views',
    (r'^author_list_plaintext/$','author_list_plaintext')
)
