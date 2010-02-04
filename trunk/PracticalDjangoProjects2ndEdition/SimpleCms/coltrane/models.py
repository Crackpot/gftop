# coding=utf8
# Create your models here.

# version 1
'''
from django.db import models
class Category(models.Model):
    title = models.CharField(max_length = 250)
    slug = models.SlugField(unique = True) # 一个简短的，有含义的文本片段，由URL中可以安全使用的字符组成。它用来生成一个特定对象的URL。方便访问者访问。
    description = models.TextField()
def __unicode__(self):
    return self.title
'''

# version 2
from django.db import models
class Category(models.Model):
    title = models.CharField(max_length = 250)
    slug = models.SlugField(unique = True) # 一个简短的，有含义的文本片段，由URL中可以安全使用的字符组成。它用来生成一个特定对象的URL。方便访问者访问。
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title
