#coding=utf8
import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from markdown import markdown
from tagging.fields import TagField


class Category(models.Model):
    title = models.CharField('标题', max_length=250,
            help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True,
            help_text="Suggested value automatically generated from title. Must be unique.")
    description = models.TextField('描述')

    class Meta:
        ordering = ['title']
        # admin页面上显示的名称
        verbose_name = '分类' # 此项不写的话会显示英文单词
        verbose_name_plural = '分类'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/weblog/categories/%s/" % self.slug
    
    def live_entry_set(self):
        from simplecms.coltrane.models import Entry
        return self.entry_set.filter(status = Entry.LIVE_STATUS)
    
class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(status = self.model.LIVE_STATUS)

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
    title = models.CharField('标题', max_length=250,
            help_text="Maximun 250 charcters.")
    excerpt = models.TextField('摘录', blank=True,
            help_text="A short summary of the entry. Optional.")
    body = models.TextField('正文')
    pub_date = models.DateTimeField('发布日期', default=datetime.datetime.now)

    # markdown生成html代码
    excerpt_html = models.TextField('摘录html', editable=False, blank=True) # editable为假时不在页面上显示
    body_html = models.TextField('正文html', editable=False, blank=True)

    # 元数据
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField('允许评论', default=True)
    featured = models.BooleanField(default=True)
    slug = models.SlugField(unique_for_date='pub_date',
            help_text="Suggested value automatically generated form title. Must be unque.")
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=LIVE_STATUS,
            help_text="Only entries with live status will be publicly displayed.")

    # 分类
    categories = models.ManyToManyField(Category)
    tags = TagField('标签', help_text="Separate tags with spaces.")

    #live = LiveEntryManager()
    objects = models.Manager() # 模板中的变量所需

    class Meta:
        ordering = ['-pub_date', 'title']
        verbose_name = '条目'
        verbose_name_plural = '条目'

    def __unicode__(self):
        return self.title

    # 重写此model的save方法
    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            # 填写了摘录
            self.excerpt_html = markdown(self.excerpt)
        else:
            # 没有填写摘录
            if self.excerpt_html:
                # 原来有摘录的话清除现有摘录
                self.excerpt_html = ''
        super(Entry, self).save(force_insert, force_update)

    def get_absolute_url(self):
        #return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
        # 对应coltrane_entry_detail通用视图
        return ('coltrane_entry_detail', (), {
            'year': self.pub_date.strftime("%Y"),
            'month': self.pub_date.strftime("%m"), # 数字月份
            #'month': self.pub_date.strftime("%b").lower(), # 月份缩写
            'day': self.pub_date.strftime("%d"),
            'slug': self.slug})
    # 基于项目现有的URL设置，permalink装饰器将会找到/weblog/前缀，并且跟随到coltrane.urls中的include()。它会找到名叫coltrane_entry_detail的模式并且用正确的值来填充那个正则表达式。
    get_absolute_url = models.permalink(get_absolute_url)

class Link(models.Model):
    # 元数据
    enable_comments = models.BooleanField('允许评论', default=True)
    post_elsewhere = models.BooleanField('发布到Delicious',
            default=True,
            help_text='如果选中,此链接将会发布到weblog和delcious帐户中。')
    posted_by = models.ForeignKey(User)
    pub_date = models.DateTimeField('发布时间', default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date',
            help_text='Must be unique for the publication date.')
    title = models.CharField('标题', max_length=250)

    # The actual link bits.
    description = models.TextField('描述', blank=True)
    description_html = models.TextField('描述html', editable=False, blank=True)
    via_name = models.CharField('Via', max_length=250, blank=True,
            help_text='The name of the person whose site you spotted the link on. Optional.')
    via_url = models.URLField('Via URL', blank=True,
            help_text='The URL of the site where you spotted the link. Optional.')
    tags = TagField('标签')
    url = models.URLField(unique=True, verify_exists=False) # 去除验证有效性

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '链接'
        verbose_name_plural = '链接'

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        if not self.id and self.post_elsewhere:
            import pydelicious
            from django.utils.encoding import smart_str
            pydelicious.add(settings.DELICIOUS_USER,
                    settings.DELICIOUS_PASSWORD,
                    smart_str(self.url), smart_str(self.title),
                    smart_str(self.tags))
        if self.description:
            # 如果有描述文本，就增加描述html
            self.description_html = markdown(self.description)
        else:
            if self.description_html:
                # 没有描述文本，但是有描述html
                self.description_html = ''
        super(Link, self).save()

    def get_absolute_url(self):
        return ('coltrane_link_detail', (),
                { 'year': self.pub_date.strftime('%Y'),
                    'month': self.pub_date.strftime('%m'),
                    #'month': self.pub_date.strftime('%b').lower(),
                    'day': self.pub_date.strftime('%d'),
                    'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)
