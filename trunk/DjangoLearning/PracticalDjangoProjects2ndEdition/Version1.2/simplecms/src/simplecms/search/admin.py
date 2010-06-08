#coding=utf8
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from simplecms.search.models import SearchKeyword

class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
    
class FlatPageAdminWithKeywords(FlatPageAdmin):
    # 内联
    inlines = [SearchKeywordInline]
    
class SearchKeywordAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(FlatPage) # 反注册此模块
admin.site.register(FlatPage, FlatPageAdminWithKeywords) # 重新注册该模块及管理类