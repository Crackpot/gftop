#coding=utf-8

from newtest.wiki.models import Wiki
from django.contrib import admin

#admin.site.register(Wiki)       #1    使用此句时候，question在上面
#class PollAdmin(admin.ModelAdmin):      #2    创建一个PollAdmin类字段fields为列表，更改了question和pub_date的顺序
#    fields=['pub_date','question']      

#class PollAdmin(admin.ModelAdmin):
#    fieldsets=[
#               (None,                 {'fields':['question']}),
#               ('Date information',     {'fields':['pub_date']}),
#    ]
#
class WikiAdmin(admin.ModelAdmin):
    fieldsets=[
               (None,{'fields':['pagename']}),
               ('Content information',{'fields':['content'],'classes':['collapse']}),
    ]

admin.site.register(Wiki,WikiAdmin)     #注册Poll对象和PollAdmin类
#
#from mysite.polls.models import Choice
#admin.site.register(Choice)
