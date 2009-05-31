#coding=utf-8
from mysite.books.models import Book,Author,Publisher
from django.contrib import admin
class BookAdmin(admin.ModelAdmin):
    list_display=('title','publisher','publication_date')
    list_filter=('publisher','publication_date')
    ordering=('-publication_date',)
    serch_fields=('title','publisher__name',)

admin.site.register(Author)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher)