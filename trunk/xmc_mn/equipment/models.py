#coding=utf8
from django.db import models
from xmc_mn.department.models import Department
    
class EquipmentCategory(models.Model):
    #设备类型
    name = models.CharField('设备类型名称', max_length=40)
    description = models.TextField('描述', max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/equipment/category/%s/" % (self.name)
    
class EquipmentParameter(models.Model):
    #设备参数 不同的设备有不同的参数，如皮带有长度、宽度
    name = models.CharField('参数类型' , max_length=40)
    parameter = models.CharField('参数值', max_length=40)
    #adscription = models.ForeignKey(Equipment, verbose_name='归属设备')
    
    def __unicode__(self):
        return self.name
    
class Equipment(models.Model):
    #设备
    name = models.CharField('设备名称', max_length=50)
    adscription = models.ForeignKey(Department, verbose_name='归属', related_name='equipment_adscription')
    location = models.ForeignKey(Department, verbose_name='所在位置', related_name='equipment_location')
    category = models.ForeignKey(EquipmentCategory, verbose_name='设备类型')
    parameter = models.ManyToManyField(EquipmentParameter, verbose_name='参数')
    
    def __unicode__(self):
        return self.name + self.category.name
    
    def getfullname(self):
        return self.name + self.category.name


