#coding=utf8
from django.contrib import admin
from models import Leixing, Canshu, Shebei, Weihujilu

class ShebeiAdmin(object):
    pass

#admin.site.register(Canshu)
admin.site.register(Leixing)
admin.site.register(Weihujilu)
admin.site.register(Shebei)