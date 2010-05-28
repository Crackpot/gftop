#coding=utf8
from django.db import models

# 所有字段都默认blank=False，这使得它们不允许输入空值。
# 允许为空和默认为NULL值就加上如此属性：blank = True, null = True

class Publisher(models.Model):
    name = models.CharField('名称', max_length = 30)
    address = models.CharField('地址', max_length = 50)
    city = models.CharField('城市', max_length = 60)
    state_province = models.CharField('省份', max_length = 50)
    country = models.CharField('国家', max_length = 50)
    website = models.URLField('网站', blank = True) # 非必须项目
    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = '出版商'
        ordering = ['name']
    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField('名', max_length = 30)
    last_name = models.CharField('姓', max_length = 40)
    email = models.EmailField('电子邮箱')
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField('书名', max_length = 100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField('出版日期')
    class Meta:
        verbose_name = '图书'
        verbose_name_plural = '图书'
        ordering = ['title', 'publisher']
    def __unicode__(self):
        return self.title
