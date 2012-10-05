#coding=utf8
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page


class Department(models.Model):
#class Department(Page):
    #部门
    name = models.CharField('部门名称', max_length=40, unique=True)#唯一键
    
    def __unicode__(self):
        return self.name

class GroupCategory(models.Model):
    name = models.CharField('类型', max_length=20)
    def __unicode__(self):
        return self.name
    
    
class Group(models.Model):
    name = models.CharField('名称', max_length=20)
    category = models.ForeignKey(GroupCategory  , verbose_name='类型')
    adscription = models.ForeignKey(Department, verbose_name='归属')
    #staffs = models.ManyToManyField(Staff, verbose_name ='职员')
    employeeno = models.IntegerField(verbose_name='员工数目')

    def __unicode__(self):
        return self.adscription.name + self.name  
    
    def staffs(self):
        return [s for s in self.staff_set.all()]
#        names = ''
#        for staff in self.staffs_set.all():
#            names = names.join(staff.name)
#        return names

    
class Staff(models.Model):
    staff = models.ForeignKey(User, blank=False, null=False, verbose_name='用户名')
    name = models.CharField('姓名', max_length=40, blank=False)
    age = models.PositiveSmallIntegerField('年龄')
    id_no = models.CharField('身份证号', max_length=18, blank=True)
    department = models.ForeignKey(Department, blank=False, null=False, verbose_name='部门')
    #group = models.ForeignKey(Group, verbose_name='班组', related_name="staffs")
    group = models.ForeignKey(Group, verbose_name='班组')
    
    def __unicode__(self):
        return self.name  
