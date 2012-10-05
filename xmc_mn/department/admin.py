#coding=utf8
from django.contrib import admin
from xmc_mn.department.models import Department, GroupCategory, Group, Staff

#class DepartmentAdmin(admin.ModelAdmin):
class GroupAdmin(admin.ModelAdmin):
    fields = ('name', ('category', 'adscription', 'employeeno'))
    list_display = ('name', 'category', 'adscription', 'staffs')
    #list_filter = ['category', 'adscription']
    
class StaffAdmin(admin.ModelAdmin): 
    fields = (('name', 'age', 'id_no'), ('department', 'group'))
    list_display = ('name', 'age', 'department')

admin.site.register(Staff, StaffAdmin)

admin.site.register(Department)
admin.site.register(GroupCategory)
admin.site.register(Group, GroupAdmin)
