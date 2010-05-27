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
import datetime

from django.contrib.auth.models import User
from django.db import models

from markdown import markdown
from tagging.fields import TagField
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length = 250,
            help_text = 'Maximum 250 characters.')
    slug = models.SlugField(unique = True,
            help_text = 'Suggested value automatically generated from title. Must be unique.') # 一个简短的，有含义的文本片段，由URL中可以安全使用的字符组成。它用来生成一个特定对象的URL。方便访问者访问。
    description = models.TextField()

    class Meta:
        ordering = ['title'] # 按标题排序
        verbose_name_plural = "Categories" # 复数

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

    def live_entry_set(self):
        from coltrane.models import Entry
        return self.entry_set.filter(status=Entry.LIVE_STATUS)

class LiveEntryManager(models.Manager):
    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)

class Entry(models.Model):
    live = LiveEntryManager()
    objects = models.Manager()
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    # Core fields.
    title = models.CharField(max_length=250,
                             help_text="Maximum 250 characters.")
    excerpt = models.TextField(blank=True,
                               help_text="A short summary of the entry. Optional.")
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    # Fields to store generated HTML.
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    # Metadata.
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique_for_date='pub_date',
            help_text="Suggested value automatically generated from title. Must be unique for the publication date.")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS,
            help_text="Only entries with live status will be publicly displayed.")

    # Categorization.
    categories = models.ManyToManyField(Category)
    tags = TagField(help_text="Separate tags with spaces.")

    objects = models.Manager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)

    def get_absolute_url(self):
        return ('coltrane_entry_detail', (), {
            'year': self.pub_date.strftime("%Y"),
            'month': self.pub_date.strftime("%b").lower(),
            'day': self.pub_date.strftime("%d"),
            'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)

class Link(models.Model):
    # 元数据
    enable_comments = models.BooleanField(default = True)
    post_elsewhere = models.BooleanField('Post to del.icio.us',
            default = True,
            help_text = 'If checked, this link will be posted both to your weblog and to your del.icio.us account.')
    posted_by = models.ForeignKey(User)
    pub_date = models.DateTimeField(default = datetime.datetime.now)
    slug = models.SlugField(unique_for_date = 'pub_date',
            help_text = 'Must be unique for the publication date.')
    title = models.CharField(max_length = 250)

    # 真正链接数据
    description = models.TextField(blank = True)
    description_html = models.TextField(blank = True)
    via_name = models.CharField('Via', max_length = 250, blank = True,
            help_text = 'The name of the person whose site you spotted the link on. Optional.')
    via_url = models.URLField('Via URL', blank = True,
            help_text = 'The URL of the site where you spotted the link. Optional.')
    tags = TagField()
    url = models.URLField('URL', unique = True)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.id and self.post_elsewhere:
            import pydelicious
            from django.utils.encoding import smart_str
            pydelicious.add(
                    settings.DELICIOUS_USER,
                    settings.DELICIOUS_PASSWORD,
                    smart_str(self.url),
                    smart_str(self.title),
                    smart_str(self.tags))
        if self.description:
            self.description_html = markdown(self.description)
        super(Link, self).save()

    def get_absolute_url(self):
        return ('coltrane_link_detail', (), {
            'year': self.pub_date.strftime('%Y'),
            'month': self.pub_date.strftime('%b').lower(),
            'day': self.pub_date.strftime('%d'),
            'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)
