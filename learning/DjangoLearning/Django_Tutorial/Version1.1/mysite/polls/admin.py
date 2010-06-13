# coding=utf8
from mysite.polls.models import Poll, Choice
from django.contrib import admin

#class ChoiceInline(admin.StackedInline): # 栈式内联
class ChoiceInline(admin.TabularInline): # 表格式内联
    model = Choice
    extra = 3 # 额外对应的数量

class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question'] # 将pub_date字段放在question之前
    # 框架集
    fieldsets = [
            (None, {'fields': ['question']}), # 没有标签，只有question一个字段
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), # 标签名称为Date information，只有pub_date一个字段，类型为折叠
            ]
    inlines = [ChoiceInline]
    #list_display = ('question', 'pub_date') # 列表显示question和pub_date两项内容
    list_display = ('question', 'pub_date', 'was_published_today') # 列表显示question，pub_date和was_published_today三项内容
    list_filter = ['pub_date'] # 基于时间的列表过滤器
    search_fields = ['question'] # 搜索域
    date_hierarchy = 'pub_date' # 时间等级

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
