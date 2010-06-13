#coding=utf8
from django.shortcuts import render_to_response
from mysite.book.models import Book
def book(request):
    books = Book.objects.all()
    return render_to_response(
            'book.html', {'books': books}
    )
