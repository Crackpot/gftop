#coding=utf8
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from models import  Yuangong

class YuangongAdmin(admin.ModelAdmin):
    search_fields = ('xingming',)
#    formfield_overrides = {
#        models.CharField: {'widget': TextInput(attrs={'size':80})},
#        models.TextField: {'widget': Textarea(attrs={'rows':8, 'cols':50})},
#    }
    
    
#    fieldsets = [
#        ('基本资料', {'fields': [
#            ('xingming', 'xingbie'), 'chushengnianyue', 'shenfenzhenghao',
#            ('jiguan', 'zhuzhi', 'zhengzhimianmao'),
#            ('rudangtuanshijian', 'lianxidianhua')
#    ]}),
#        ('工作情况', {'fields':['cangongshijian', 'baoxianhao', 'renshikahao']}),
##        ('Date information', {'fields': ['chushengnianyue']}),
#    ]

admin.site.register(Yuangong, YuangongAdmin)
