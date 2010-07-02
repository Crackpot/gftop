#coding=utf8
import datetime
from django.db import models
from pygments import formatters, highlight, lexers
from markdown import markdown
from tagging.fields import TagField
from django.contrib.auth.models import User
from simplecms.cab import managers

class Language(models.Model):
    name = models.CharField('名称', max_length = 100)
    slug = models.SlugField(unique = True)
    language_code = models.CharField('语言代码', max_length = 50)
    mime_type = models.CharField('mime类型', max_length = 100)

    class Meta:
        ordering = ['name']
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ('cab_language_detail', (), {'slug': self.slug})
    get_absolute_url = models.permalink(get_absolute_url)

    def get_lexer(self):
        return lexers.get_lexer_by_name(self.language_code)

    objects = managers.LanguageManager()


class Snippet(models.Model):
    title = models.CharField('标题', max_length = 255)
    language = models.ForeignKey(Language)
    author = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable = False)
    code = models.TextField()
    highlighted_code = models.TextField(editable = False)
    tags = TagField()
    pub_date = models.DateTimeField(editable = False)
    updated_date = models.DateTimeField(editable = False)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.title

    def save(self, force_insert = False, force_update = False):
        if not self.id:
            self.pub_date = datetime.datetime.now()
        self.updated_date = datetime.datetime.now()
        self.description_html = markdown(self.description)
        self.highlighted_code = self.highlight()
        super(Snippet, self).save(force_insert, force_update)

    def get_absolute_url(self):
        return ('cab_snippet_detail', (), {'object_id': self.id})
    get_absolute_url = models.permalink(get_absolute_url)

    def highlight(self):
        return highlight(self.code,
                         self.language.get_lexer(),
                         formatters.HtmlFormatter(linenos=True))

    objects = managers.SnippetManager()

class Bookmark(models.Model):
    snippet = models.ForeignKey(Snippet)
    user = models.ForeignKey(User, related_name = 'cab_bookmarks')
    date = models.DateTimeField(editable = False)
    
    class Meta:
        ordering = ['-date']
    def __unicode__(self):
        return "%s bookmarked by %s" % (self.snippet, self.user)
    def save(self):
        if not self.id:
            self.date = datetime.datetime.now()
        super(Bookmark, self).save()
