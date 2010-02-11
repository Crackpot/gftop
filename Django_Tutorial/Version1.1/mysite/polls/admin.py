# coding=utf8
from django.contrib import admin
from mysite.polls.models import Poll, Choice

# 在Poll的显示页面上添加三个额外的Choice字段
#class ChoiceInline(admin.StackedInline): # 栈式内联
class ChoiceInline(admin.TabularInline): # 表格式内联
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question'] # 将pub_date字段移上
    '''
    # 字段集，用一个列表来表示，元组中的第一个元素为标题显示内容。
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    '''

    # 另一种字段集的表示方法，用collapse类型显示
    fieldsets = [
            (None, {'fields': ['question']}),
            ('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),
            ]
    list_display = ('question', 'pub_date', 'was_published_today') # polls列表显示页面中显示question，pub_date, was_published_today三个字段
    inlines = [ChoiceInline] # 内联
    list_filter = ['pub_date'] # 以时间为基准的列表过滤器
    search_fields = ['question'] # 搜索框
    date_hierarchy = 'pub_date' # 时间等级链接

class ChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
