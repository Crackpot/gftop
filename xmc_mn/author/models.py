#coding=utf8
from django.db import models
from mezzanine.pages.models import Page

# The members of Page will be inherited by the Author model, such
# as title, slug, etc. For authors we can use the title field to
# store the author's name. For our model definition, we just add
# any extra fields that aren't part of the Page model, in this
# case, date of birth.

class Author(Page):
    dob = models.DateField("Date of birth")
    class Meta:
        app_label = u"1图书"
        verbose_name = '作者'
        verbose_name_plural = '作者'
        db_table = 'author_author'

class Book(models.Model):
    author = models.ForeignKey("Author")
    cover = models.ImageField(upload_to="uploads/authors")
    class Meta:
        app_label = u"1图书"
        verbose_name = '图书'
        verbose_name_plural = '图书'
        db_table = 'author_book'