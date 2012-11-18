#coding=utf8
from django.db import models

class Danwei(models.Model):
    danwei = models.CharField('单位', max_length=20, primary_key=True, unique=True, help_text='队组及其他单位名称,不可重复')

    def __unicode__(self):
        return self.danwei

#    class Meta:
#        app_label = u"员工"
#        verbose_name = '单位'
#        verbose_name_plural = '单位'
#        db_table = 'yuangong_danwei'
