#coding=utf8
from django.db import models
from datetime import datetime
from django.utils import timezone
from xmc_dj.settings import MEDIA_ROOT

class Material(models.Model):
    number = models.CharField('序号', max_length=40, blank=False) #序号
    name = models.CharField('名称', max_length=128, blank=False) #名称
    factory = models.CharField('厂家', max_length=128, blank=False) #厂家
    amount = models.IntegerField('数量', blank=False) #数量
    dimension = models.CharField('幅面', max_length=20) #幅面
    archived_time = models.DateTimeField('存档时间', blank=False) #存档时间
    utilizing = models.CharField('使用地点', max_length=20) #使用地点
    remark = models.TextField('备注', blank=True, null=True) #备注
    front_cover = models.ImageField('封面', upload_to='upload/frontcover/%Y/%m/%d', blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class Lending(models.Model):
    material = models.ForeignKey(Material, verbose_name='资料名称')
    amount = models.IntegerField('数目', blank=False)
    borrower = models.CharField('借阅人', max_length=128, blank=False)
    lender = models.CharField('借出人', max_length=128, blank=False)
    deposit = models.IntegerField('押金', blank=False)
    borrowed_time = models.DateTimeField('借阅时间', blank=False)
    return_time = models.DateTimeField('归还时间', blank=True, null=True)
    
    #判断是否已归还
    def was_returned(self):
        if self.return_time!= None:
            return self.return_time >= timezone.now()
        else:
            return False
        
    was_returned.admin_order_field = 'return_time'
    was_returned.short_description = '已还'

    
    def __unicode__(self):
        return self.material.name
