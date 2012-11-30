#coding=utf8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField, USStateField
from django.contrib.localflavor.cn.cn_provinces import CN_PROVINCE_CHOICES


class Customer(models.Model):
    '''
    The ``Customer`` model represents a customer of the online
    store. It wraps Django's built-in ``auth.User`` model, which
    contains information like first and last name, and email, and adds
    phone number and address information.
    '''
    user = models.ForeignKey(User)
    address = models.ForeignKey('CustomerAddress')
    phone_number = PhoneNumberField(blank=True)

class CustomerAddress(models.Model):
    '''
    The ``CustomerAddress`` model represents a customer's address. It
    is slightly biased in favor of US addresses, but should contain
    enough fields to represent addresses in other countries.
    '''
    line_1 = models.CharField(max_length=300)
#    line_2 = models.CharField(max_length=300)
#    line_3 = models.CharField(max_length=300)
    city = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=10)
    #state = USStateField(blank=True)
    #中国省份
    province = models.CharField(max_length =6, choices = CN_PROVINCE_CHOICES, blank = True)
    country = models.CharField(max_length=150)
    