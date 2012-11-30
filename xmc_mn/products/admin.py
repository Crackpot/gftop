#coding=utf8
from django.contrib import admin
from products.models import *


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'publisher', 'description', 'pub_date')
admin.site.register(Catalog, CatalogAdmin)

class CatalogCategoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'description', 'parent')
admin.site.register(CatalogCategory, CatalogCategoryAdmin)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('product', 'attribute', 'value')
admin.site.register(ProductDetail, ProductDetailAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
admin.site.register(ProductAttribute, ProductAttributeAdmin)