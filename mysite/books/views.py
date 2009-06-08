#coding=utf-8
# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from models import Book
from forms import ContactForm 
#from forms import PublisherForm


def search(request):
    query=request.GET.get('q','')
    if query:
        qset=(
            Q(title__icontains=query)|
            Q(authors__first_name__icontains=query)|
            Q(authors__last_name__icontains=query)
        )
        results=Book.objects.filter(qset).distinct()
    else:
        results=[]
    return render_to_response('books/search.html',{
        'results':results,
        'query':query
    })
    
def search_form(request):
    errors=[]
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('请输入一个搜索条目！')
        elif len(q)>20:
            errors.append('搜索条目不能超过20个字符！')
        else:
            books=Book.objects.filter(title__icontains=q)
            return render_to_response('books/search_results.html',
                {'books':books,'query':q}
            )
    return render_to_response('books/search_form.html',
        {'errors':errors}
    )
    
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            topic=form.cleaned_data['topic']
            message=form.cleaned_data.get('message')
            sender=form.cleaned_data.get('sender','noreply@example.com')
            send_mail(
                'Feedback from your site, topic: %s' % topic,
                message, sender,
                ['gaofeitop@gmail.com']
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form=ContactForm()
    return render_to_response('contact.html',{'form':form})

def contact_form(request):
    errors=[]
    if request.method=='POST':
        if not request.POST.get('subject',''):
            errors.append('主题不可为空！')
        if not request.POST.get('message',''):
            errors.append('内容不可为空！')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('请输入一个有效的邮件地址')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email','gaofeitop@gmail.com'),
                ['gaofeitop@crackpot.com'],
            )
            return HttpResponse('/contact_form/thanks/')
    return render_to_response('contact_form.html',{
        'errors':errors,
        'subject':request.POST.get('subject',''),
        'message':request.POST.get('message',''),
        'email':request.POST.get('email',''),
    })

def add_publisher(request):
    if request.method=='POST':
        form=PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_publisher/thanks/')
        else:
            form=PublisherForm()            
        return render_to_response('books/add_publisher.html',{'form':form})
    
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

def about_pages(request, page):
    try:
        return direct_to_template(request, template="about/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()
    
    
    
from django.http import Http404
from django.views.generic import list_detail
from mysite.books.models import Book, Publisher

def books_by_publisher(request, name):
    # Look up the publisher (and raise a 404 if it can't be found).
    try:
        publisher = Publisher.objects.get(name__iexact=name)
    except Publisher.DoesNotExist:
        raise Http404

    # Use the object_list view for the heavy lifting.
    return list_detail.object_list(
        request,
        queryset = Book.objects.filter(publisher=publisher),
        template_name = "books/books_by_publisher.html",
        #template_object_name = "books",#有这句将得不到结果
        extra_context = {"publisher" : publisher}
    )

import datetime
from mysite.books.models import Author
from django.views.generic import list_detail
from django.shortcuts import get_object_or_404

def author_detail(request, author_id):
    # Look up the Author (and raise a 404 if she's not found)
    author = get_object_or_404(Author, pk=author_id)

    # Record the last accessed date
    author.last_name = datetime.datetime.now()
    author.save()

    # Show the detail page
    return list_detail.object_detail(
        request,
        queryset = Author.objects.all(),
        object_id = author_id,
        template_name='books/author_detail.html',
        extra_context={'author':author}
    )


def author_list_plaintext(request):
    response = list_detail.object_list(
        request,
        queryset = Author.objects.all(),
        mimetype = "text/plain",
        template_name = "books/author_list.txt"
    )
    response["Content-Disposition"] = "attachment; filename=authors.txt"
    return response
