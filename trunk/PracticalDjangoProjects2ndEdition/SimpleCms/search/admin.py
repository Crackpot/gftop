# coding=utf8

# version 1
'''
from django.contrib import admin
from SimpleCms.search.models import SearchKeyword
class SearchKeywordAdmin(admin.ModelAdmin):
    pass
admin.site.register(SearchKeyword, SearchKeywordAdmin)
'''

# version 2
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from SimpleCms.search.models import SearchKeyword

class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
class SearchKeywordAdmin(admin.ModelAdmin):
    pass
class FlatPageAdminWithKeywords(FlatPageAdmin):
    # 在简单页面下边显示关键词列表框
    inlines = [SearchKeywordInline]
admin.site.unregister(FlatPage)
admin.site.register(SearchKeyword, SearchKeywordAdmin)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)
