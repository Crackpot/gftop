#coding=utf8
from django.contrib import admin
from customers.models import *

admin.site.register(Customer)
admin.site.register(CustomerAddress)