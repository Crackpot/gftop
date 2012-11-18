#coding=utf8
from django.contrib import admin
from models import Leixing, Shebei

class ShebeiAdmin(object):
    pass

admin.site.register(Leixing)
admin.site.register(Shebei)