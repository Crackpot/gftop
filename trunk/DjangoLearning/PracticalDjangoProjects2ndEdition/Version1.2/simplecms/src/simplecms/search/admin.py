#coding=utf8
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from simplecms.search.models import SearchKeyword

class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
    
class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]
    
class SearchKeywordAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)