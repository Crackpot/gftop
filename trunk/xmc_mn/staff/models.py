#coding=utf8
from django.contrib.auth.models import User
from django.db import models
from xmc_mn.department.models import Group
#from xmc_mn.department.models import Department

class Staff(models.Model):
    staff = models.ForeignKey(User, blank=False, null=False)
    name = models.CharField(max_length=40, blank=False)
    age = models.IntegerField()
    id_no = models.CharField(max_length=18, blank=True)
    #department = models.ForeignKey(Department, blank =False, null = False)
    group = models.ForeignKey(Group, verbose_name='班组')
