#coding=utf8
from mysite.polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline): #admin.StackedInline占地太大
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    # fieldsets 中每个元组的第一个元素就是组的标题。
    fieldsets = [
        (None, {'fields':['question']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    
class ChoiceAdmin(admin.ModelAdmin):    
    pass

admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice, ChoiceAdmin)
