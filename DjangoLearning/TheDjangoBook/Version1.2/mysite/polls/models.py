#coding=utf8
from django.db import models
import datetime

# Create your models here.
class Poll(models.Model):
    question = models.CharField('问题', max_length = 200)
    pub_date = models.DateTimeField('发布日期')
    def __unicode__(self):
        return self.question
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
    def get_absolute_url(self):
        return "/polls/%i/"% self.id
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll) # 外键
    choice = models.CharField('选择', max_length = 200)
    votes = models.IntegerField('票数')
    def __unicode__(self):
        return self.choice