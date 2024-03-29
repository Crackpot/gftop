from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering=['name']
        
class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField('e-mail',blank=True)
    last_accessed=models.DateField()
    headshot = models.ImageField(upload_to='/home/workspace/gftop/mysite/books/headshots')
    def __unicode__(self):
        return u'%s %s'%(self.first_name,self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True,null=True)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering=['title']
