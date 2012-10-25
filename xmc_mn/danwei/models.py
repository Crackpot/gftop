#coding=utf8
from django.db import models

class Danwei(models.Model):
    title = models.CharField('单位', max_length = 20)
    
    def __unicode__(self):
        return self.title