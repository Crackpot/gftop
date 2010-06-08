#coding=utf8
from django import forms
from mysite.books.models import Book, Publisher

class BookForm(forms.ModelForm):
    class Meta:
        model = Book

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher