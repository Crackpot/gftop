#coding=utf8
from django.forms import ModelForm
from mysite.books.models import Book, Publisher

class BookForm(ModelForm):
    class Meta:
        model = Book

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher    