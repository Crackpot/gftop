#coding=utf8
from mysite.blog.models import BlogPost
from django.contrib import admin

class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','body','timestamp')
    
admin.site.register(BlogPost, BlogPostAdmin)