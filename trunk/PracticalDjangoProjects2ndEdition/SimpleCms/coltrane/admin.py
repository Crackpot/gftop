# coding=utf8

# version 1
'''
from django.contrib import admin
from coltrane.models import Category
class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)
'''

# version 2
from django.contrib import admin
from coltrane.models import Category
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }
admin.site.register(Category, CategoryAdmin)
