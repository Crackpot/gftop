#coding=utf8
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ("-timestamp",)