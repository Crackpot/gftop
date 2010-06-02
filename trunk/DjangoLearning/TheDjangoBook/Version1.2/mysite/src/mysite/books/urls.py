#coding=utf8
from django.conf.urls.defaults import *
from mysite.books import views
urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^publishers/(\d+)/$', views.publisher_detail),
    (r'^publishers/(\d+)/edit/$', views.publisherEdit),
    (r'^books/(\d+)/$', views.book_detail),
    (r'^books/(\d+)/edit/$', views.bookEdit),
    (r'^search/$', views.search),
    #(r'^(?P<id>\d*)/$', views.BookEdit),
)

# 下面使用通用视图
from django.views.generic import list_detail
from mysite.books.models import Author, Book, Publisher

author_info = {
    'queryset': Author.objects.all(),
    'template_name': 'books/list_authors.html'
}

book_info = {
    #'queryset': Book.objects.all(), # 获取全部图书
    'queryset': Book.objects.order_by('-publication_date'), # 按照出版日期排序，最近的排在最前
    'template_name': 'books/list_books.html',
}

publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'books/list_publishers.html',
    #'template_object_name': 'publisher',
    
    # 此函数后面并没有括号，说明是一个函数的引用，并没有真正调用它，只是在渲染的时候调用
    #'extra_context': {'book_list': Publisher.get_books}
}
urlpatterns += patterns('',
    (r'^books/$', list_detail.object_list, book_info), # 图书
    (r'^authors/$', list_detail.object_list, author_info), # 作者
    (r'^publishers/$', list_detail.object_list, publisher_info), # 出版社
)
