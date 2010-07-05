#coding=utf8
from django.contrib import admin
from simplecms.cab.models import Bookmark, Language, Snippet 

class BookmarkAdmin(admin.ModelAdmin):
    pass
class LanguageAdmin(admin.ModelAdmin):
    pass
class SnippetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Snippet, SnippetAdmin)