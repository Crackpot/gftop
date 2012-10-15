#coding=utf8
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Book
from books.forms import ContactForm

def latest_books(request):
    book_list = Book.objects.order_by('-publication_date')[:10]
    return render_to_response('books/latest_books.html', {'book_list': book_list})

def book_list(request):
    books = Book.objects.order_by('name')
    return render_to_response('books/book_list.html', {'books': books})

def search_form(request):
    return render_to_response('books/search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('books/search_results.html',
                {'books': books, 'query': q})
    return render_to_response('books/search_form.html',
        {'errors': errors})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('books/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render_to_response('books/contact_form.html', {'form': form})