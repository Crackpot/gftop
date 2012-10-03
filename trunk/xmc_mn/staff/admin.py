#coding=utf8
from django.contrib import admin
from xmc_mn.staff.models import Staff

class StaffAdmin(admin.ModelAdmin): 
    list_display = ('name', 'age')

admin.site.register(Staff, StaffAdmin)
