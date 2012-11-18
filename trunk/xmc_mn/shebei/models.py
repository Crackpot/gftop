#coding=utf8
from django.db import models
from danwei.models import Danwei

class Leixing(models.Model):
    leixing = models.CharField('类型', max_length=20, unique=True)
    
    def __unicode__(self):
        return self.leixing

class WeihuJilu(models.Model):
    shijian = models.DateTimeField('维护时间')
    neirong = models.TextField('内容')
    
class Shebei(models.Model):
    xuhao = models.CharField('序号', max_length=20, unique=True, help_text='设备序号')
    mingcheng = models.CharField('名称', max_length=20, unique=True)
    bianhao = models.CharField('编号', max_length=20, unique=True)
    leixing = models.ForeignKey(Leixing, verbose_name='设备类型')
    suoshu = models.ForeignKey('danwei.Danwei', verbose_name='设备所属')
    
    def __unicode__(self):
        return self.mingcheng
