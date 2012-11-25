#coding=utf8

from django.contrib import admin
from models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors', 'publisher', 'publication_date')
    #fields = ('title', 'authors', 'publisher')
    filter_horizontal = ('authors',)
    #raw_id_fields = ('publisher',) # 前面是数字，后面是搜索
    
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
