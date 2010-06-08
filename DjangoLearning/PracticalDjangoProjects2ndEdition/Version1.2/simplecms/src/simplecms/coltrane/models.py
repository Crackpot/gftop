#coding=utf8
from django.db import models

class  Category(models.Model):
    title = models.CharField('标题', max_length = 250,  help_text='Maximum 250 characters.')
    slug = models.SlugField(unique = True,
        help_text = "Suggested value automatically generated from title. Must be unique.")
    description = models.TextField('描述')
    
    class Meta:
        ordering = ['title']
        # admin页面上显示的名称
        verbose_name = '分类'
        verbose_name_plural = '分类'
        
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/categories/%s/" % self.slug
    
class Entry(models.Model):
    title = models.CharField('标题', max_length = 250)
    excerpt = models.TextField('摘录', blank = True)
    body = models.TextField('正文')
    pub_date = models.DateTimeField('发布日期')