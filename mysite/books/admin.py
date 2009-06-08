#coding=utf-8
from mysite.books.models import Book,Author,Publisher
from django.contrib import admin
class BookAdmin(admin.ModelAdmin):
    list_display=('title','publisher','publication_date')
    list_filter=('publisher','publication_date')
    date_hierarchy='publication_date'
    ordering=('-publication_date',)
    serch_fields=('title','publisher__name',)
    fields=('title','authors','publisher','publication_date')
    filter_horizontal=('authors',)
    raw_id_fields=('publisher',)
    
class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','last_accessed')
    search_fields=('first_name','last_name')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher)