#coding=utf8
import datetime

from django.contrib.auth.models import User
from django.db import models

from markdown import markdown
from tagging.fields import TagField

class  Category(models.Model):
    title = models.CharField('标题', max_length = 250,
            help_text='Maximum 250 characters.')
    slug = models.SlugField(unique = True,
            help_text = "Suggested value automatically generated from title. Must be unique.")
    description = models.TextField('描述')

    class Meta:
        ordering = ['title']
        # admin页面上显示的名称
        verbose_name = '分类' # 此项不写的话会显示英文单词
        verbose_name_plural = '分类'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

class Entry(models.Model):
    # 条目状态
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    # 关键字段
    title = models.CharField('标题', max_length = 250,
            help_text = "Maximun 250 charcters.")
    excerpt = models.TextField('摘录', blank = True,
            help_text = "A short summary of the entry. Optional.")
    body = models.TextField('正文')
    pub_date = models.DateTimeField('发布日期', default = datetime.datetime.now)

    # markdown生成html代码
    excerpt_html = models.TextField('摘录html', editable = False, blank = True) # editable为假时不在页面上显示
    body_html = models.TextField('正文html', editable = False, blank = True)

    # 元数据
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField('允许评论', default = True)
    featured = models.BooleanField(default = True)
    slug = models.SlugField(unique_for_date = 'pub_date',
            help_text = "Suggested value automatically generated form title. Must be unque.")
    status = models.IntegerField('状态', choices = STATUS_CHOICES, default = LIVE_STATUS,
            help_text = "Only entries with live status will be publicly displayed.")

    # 分类
    categories = models.ManyToManyField(Category)
    tags = TagField('标签', help_text = "Separate tags with spaces.")

    class Meta:
        ordering = ['-pub_date', 'title']
        verbose_name = '条目'
        verbose_name_plural = '条目'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

    # 重写此model的save方法
    def save(self, force_insert = False, force_update = False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)
