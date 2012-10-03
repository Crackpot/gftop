#coding=utf8
from django.contrib import admin
from xmc_mn.equipment.models import Equipment, Category

class EquipmentAdmin(admin.ModelAdmin):
    #列表显示
    list_display = ('name', 'adscription', 'category', 'location')
    list_display_link= ('name', 'adscription', 'category')
    search_fields = ['name']
    list_filter = ['adscription', 'category', 'location']
    


class CategoryAdmin(admin.ModelAdmin):
    #列表显示
    list_display = ('name', 'description')
    
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Category, CategoryAdmin)
