#coding=utf8
from django.contrib import admin
from xmc_mn.material.models import Dimension,  Material, Lending
class DimensionAdmin(admin.ModelAdmin):
    list_display = ('name', 'dimension')

class MaterialAdmin(admin.ModelAdmin):
    #列表显示
    list_display = ('name', 'number', 'factory', 'utilizing', 'amount', 'archived_time')
    list_display_links = ('name', 'number', 'factory', 'utilizing', 'amount', 'archived_time')
    #搜索域
    search_fields = ['name', 'number', 'factory', 'utilizing']
    #时间条
    date_hierarchy = 'archived_time'
    list_filter = ['factory', 'utilizing']
#    class Media:
#        js = [
#              '/static/jscripts/tiny_mce/tiny_mce.js',
#              '/media/editor/tiny_mce/tiny_mce_src.js',
#              '/media/editor/tiny_mce/tiny_mce_config.js',
#        ]


    
class LendingAdmin(admin.ModelAdmin):
    #列表显示
    list_display = ('material', 'amount', 'borrower', 'lender', 'borrowed_time', 'return_time', 'was_returned')
    list_display_links = ('material', 'amount', 'borrower', 'lender', 'borrowed_time', 'return_time', 'was_returned')
    fieldsets = [
        ('资料外借基本情况', {'fields': ['material', 'amount', 'deposit']}),
        ('借阅人及借出人', {'fields': ['borrower', 'lender']}),
        ('借阅及其归还时间', {'fields': ['borrowed_time', 'return_time']}),
    ]
    #搜索域
    search_fields = ['material', 'borrower', 'lender']
    #时间条
    date_hierarchy = 'borrowed_time'

    
admin.site.register(Dimension, DimensionAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Lending, LendingAdmin)
