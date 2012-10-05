#coding=utf8
from django.contrib import admin
from xmc_mn.equipment.models import Equipment, EquipmentCategory

#class EquipmentInline(admin.StackedInline):
#    model = Equipment.photograph
#    extra = 3

class EquipmentAdmin(admin.ModelAdmin):
    #列表显示
    #list_display = ('name', 'adscription', 'category', 'location', 'parameter')
    fields = [('name', 'category', 'adscription', 'location'), 'parameter', 'photograph'] #分组显示
    list_display_link = ('name', 'adscription', 'category')
    search_fields = ['name']
    list_filter = ['adscription', 'category', 'location']
    search_fields = ['name', 'adscription__name', 'category__name', 'location__name', 'parameter'] #搜索
#    inlines = [ChoiceInline]

class EquipmentCategoryAdmin(admin.ModelAdmin):
    #列表显示
    list_display = ('name', 'description')
    
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentCategory, EquipmentCategoryAdmin)
#admin.site.register(EquipmentParameter)
