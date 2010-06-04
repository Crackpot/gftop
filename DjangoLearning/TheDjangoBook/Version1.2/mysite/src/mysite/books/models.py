#coding=utf8
from django.db import models
import datetime

# 所有字段都默认blank=False，这使得它们不允许输入空值。
# 允许为空和默认为NULL值就加上如此属性：blank = True, null = True

class Publisher(models.Model):
    name = models.CharField('名称', max_length=30, unique=True) # 唯一
    country = models.CharField('国家', max_length=50)
    state_province = models.CharField('省份', max_length=50)
    city = models.CharField('城市', max_length=60)
    address = models.CharField('地址', max_length=50)
    website = models.URLField('网站', blank=True, help_text='非必须项目') # 非必须项目
    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = '出版商'
        ordering = ['name']
    def __unicode__(self):
        return self.name
    def get_books(self):
        return Book.objects.filter(publisher__id=self.id)
    def get_absolute_url(self):
        return "/books/publishers/%i/" % self.id


class Author(models.Model):
    name = models.CharField('姓名', max_length=30)
    email = models.EmailField('电子邮箱', unique=True)
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'
    def __unicode__(self):
        return self.name
        #return u'%s %s' % (self.last_name, self.first_name)
    def get_absolute_url(self):
        return "/books/authors/%i/" % self.id
    
class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class Book(models.Model):
    title = models.CharField('书名', unique = True , max_length=100)
    authors = models.ManyToManyField(Author) # 多对多关系
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField('出版日期', default=datetime.datetime.date(datetime.datetime.today())) # 默认值为今天日期
    num_pages = models.IntegerField('页数')
    objects = BookManager() 
    def get_authors(self):
        string = ''
        for author in self.authors.all():
            string += str(author) + ' '
        return string
    class Meta:
        verbose_name = '图书'
        verbose_name_plural = '图书'
        ordering = ['id', 'title', 'publisher']
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/books/books/%i/" % self.id
    
class BookAuthor(models.Model):
    book = models.ForeignKey(Book)
    author = models.ForeignKey(Author)
