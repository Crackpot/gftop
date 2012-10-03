#coding=utf8
from django.db import models
from xmc_mn.department.models import Department
    
class Category(models.Model):
    name = models.CharField('设备类型名称', max_length=40)
    description = models.TextField('描述', max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/equipment/category/%s/" % (self.name)
    
class Equipment(models.Model):
    name = models.CharField('设备名称', max_length=50)
    adscription = models.ForeignKey(Department, verbose_name='归属', related_name='equipment_adscription')
    location = models.ForeignKey(Department, verbose_name='所在位置', related_name='equipment_location')
    category = models.ForeignKey(Category, verbose_name="设备类型")
    
    def __unicode__(self):
        return self.name + self.category.name
    
    def getfullname(self):
        return self.name + self.category.name
