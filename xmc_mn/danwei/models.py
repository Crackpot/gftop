#coding=utf8
from django.db import models

class Danwei(models.Model):
    danwei = models.CharField('单位', max_length = 20, unique=True)

    def __unicode__(self):
        return self.danwei
    
    class Meta:
        ordering = ['id']
#        app_label = u"单位"
#        verbose_name = '单位'
#        verbose_name_plural = '单位'
#        db_table = 'danwei_danwei'