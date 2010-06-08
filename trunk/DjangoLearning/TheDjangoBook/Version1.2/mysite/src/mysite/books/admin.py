#coding=utf8
from mysite.books.models import Publisher, Author, Book
from django.contrib import admin

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    
def authors(Book):
    return str(Book.authors.all())

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', authors , 'publisher', 'num_pages' , 'publication_date')
    list_filter = ('publication_date', 'publisher')
    # 搜索域
    search_fields = ('title', 'publisher__name') # 通过外键找到Publisher的name
    # 日期层次划分
    date_hierarchy = 'publication_date'
    # 必须是元组，记得加逗号
    ordering = ('-publication_date',)
    # 创建与修改图书信息需要填写的字段，按照以下的顺序显示
    fields = ('title', 'authors', 'publisher', 'num_pages', 'publication_date') # 可以去掉publication_date，防止被编辑
    # 列表选择框
    filter_horizontal = ('authors',) # 水平选择框，占用位置较小
    #filter_vertical = ('authors',) # 竖直选择框，占用位置较大
    raw_id_fields = ('publisher',) # 一个包含外键字段名称的元组，它包含的字段将被展现成文本框 ，而不再是下拉框 
    
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)