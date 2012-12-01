#coding=utf8

from django.contrib import admin
from models import Danwei

class DanweiAdmin(admin.ModelAdmin):
    ordering = ('id',)

admin.site.register(Danwei )