import datetime
from django.db import models

from django.db import models
from django.contrib import admin

import tagging

class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    @models.permalink
    def get_absolute_url(self):
        return ('items_view_item', [self.id])
    
    def __unicode__(self):
        return self.name

tagging.register(Item)
admin.site.register(Item)
