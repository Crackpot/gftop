#coding=utf8
from django.db import models

class Tongzhi(models.Model):
    zhuti = models.CharField('主题', max_length = 100)
    tongzhi = models.CharField('通知',max_length = 500)
    fabushijian = models.DateTimeField('发布时间')
    
    def __unicode__(self):
        return self.zhuti