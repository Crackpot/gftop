#coding=utf-8
from djangobooks.books.models import Book ,Author,Publisher
from django.contrib import admin
class BookAdmin(admin.ModelAdmin):
    list_display=('title','publisher','publication_date',)
    list_filter=('publisher','publication_date',)
    ordering=('-publication_date',)
    search_fields=('title','publisher__name',)      #做 Django Admin 时出现了 Related Field has invalid lookup: icontains。原来外键是需要指定相应的字段的。外键不只是一个字段，是另一个表的完整一行。所以我们需要指定特定的字段 "本表外键字段__外键所在表需查询字段"
    
admin.site.register(Author)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher)