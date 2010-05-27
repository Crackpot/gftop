#coding=utf8
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    num_pages = models.IntegerField()
    authors = models.ManyToManyField(Author)
    def __unicode__(self):
        return self.title
