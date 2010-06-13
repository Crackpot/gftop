#coding=utf8
from django.contrib import admin
from simplecms.coltrane.models import Category, Entry, Link

class CategoryAdmin(admin.ModelAdmin):
    # 预填充的域
    prepopulated_fields = {'slug': ['title']}

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    pass

class LinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Link, LinkAdmin)