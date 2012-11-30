#coding=utf8
from danwei.models import Danwei
from django.db import models

class Leixing(models.Model):
    leixing = models.CharField('类型', max_length=20, unique=True)
    
    def __unicode__(self):
        return self.leixing
    
class Canshu(models.Model):
    canshu = models.CharField('参数', max_length = 100)
        
#    class Meta:
#        abstract = True
    
class Shebei(models.Model):
    xuhao = models.CharField('序号', max_length=20, unique=True, help_text='设备序号')
    mingcheng = models.CharField('名称', max_length=20, unique=True)
    bianhao = models.CharField('编号', max_length=20, unique=True)
    leixing = models.ForeignKey(Leixing, verbose_name='设备类型')
    suoshu = models.ForeignKey(Danwei, verbose_name='设备所属')
    #canshu = models.ManyToManyField(Canshu, verbose_name = '参数')
    
    def __unicode__(self):
        return self.mingcheng + self.leixing.leixing
    
    def get_absolute_url(self):
        return "/shebei/%i/" % self.mingcheng

class Weihujilu(models.Model):
    shebei = models.ForeignKey(Shebei, verbose_name='设备')
    shijian = models.DateTimeField('维护时间')
    neirong = models.TextField('内容')
    
    def __unicode__(self):
        return u'%s%s维护' % (self.shebei.mingcheng , self.shebei.leixing.leixing)
