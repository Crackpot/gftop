#coding=utf8
from django.contrib import admin
from xmc_mn.department.models import Department, GroupCategory, Group, Staff

#class DepartmentAdmin(admin.ModelAdmin):
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'adscription', 'staffs')
    list_filter = ['category', 'adscription']
    
class StaffAdmin(admin.ModelAdmin): 
    list_display = ('name', 'age')

admin.site.register(Staff, StaffAdmin)

admin.site.register(Department)
admin.site.register(GroupCategory)
admin.site.register(Group, GroupAdmin)
