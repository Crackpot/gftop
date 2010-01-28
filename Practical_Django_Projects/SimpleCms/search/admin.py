# coding=utf8
from django.contrib import admin
from SimpleCms.search.models import SearchKeyword

class SearchKeywordAdmin(admin.ModelAdmin):
    pass
admin.site.register(SearchKeyword, SearchKeywordAdmin)
