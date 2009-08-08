#coding=utf-8
from django.db import models

# Create your models here.
class Wiki(models.Model):
    pagename = models.CharField(max_length=20, unique=True)     #max_length不要忘记中间的连接附
    content = models.TextField()
