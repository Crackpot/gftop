#coding=utf8
'''
Models file for the `products` coleman app. These models represent
basic product and catalog information for an ecommerce
application. They are designed to be pluggable and reusable in any
Django project.
'''
from datetime import datetime
from django.db import models


class Catalog(models.Model):
    '''
    The ``Catalog`` model represents a collection of products for
    sale. A catalog contains additional information like name,
    publisher, a short description, and a publication date.
    '''
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    publisher = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return u'%s' % self.name

class CatalogCategory(models.Model):
    '''
    The ``Category`` model represents a category within a specific
    ``Catalog`` object. Categories contain a ForeignKey to their
    catalog, as well as an optional ForeignKey to another category
    that will serve as a parent category.
    '''
    catalog = models.ForeignKey('Catalog', related_name='categories')
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)

    def __unicode__(self):
        if self.parent:
            return u'%s: %s - %s' % (self.catalog.name,
                                     self.parent.name,
                                     self.name)
        return u'%s: %s' % (self.catalog.name, self.name)

class Product(models.Model):
    '''
    The ``Product`` model represents a particular item in a catalog of
    products. It contains information about the product for sale,
    which is common to all items in the catalog. These include, for
    example, the item's price, manufacturer, an image or photo, a
    description, etc.
    '''
    category = models.ForeignKey('CatalogCategory', related_name='products')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='uploads/product_photo', blank=True)
    manufacturer = models.CharField(max_length=300, blank=True)
    price_in_dollars = models.DecimalField(max_digits=6, decimal_places=2)
    price_in_euros = models.DecimalField(max_digits=6, decimal_places=2)
    price_in_pounds = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return u'%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('product_detail', (), {'slug': self.slug})
    
class ProductDetail(models.Model):
    '''
    The ``ProductDetail`` model represents information unique to a
    specific product. This is a generic design that can be used to
    extend the information contained in the ``Product`` model with
    specific, extra details.
    '''
    product = models.ForeignKey('Product', related_name='details')
    attribute = models.ForeignKey('ProductAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.product, self.attribute)

class ProductAttribute(models.Model):
    '''
    The ``ProductAttribute`` model represents a class of feature found
    across a set of products. It does not store any data values
    related to the attribute, but only describes what kind of a
    product feature we are trying to capture.

    Possible attributes include things like materials, colors, sizes,
    and many, many more.
    '''
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name