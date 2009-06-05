#coding=utf-8
# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from models import Book
from forms import ContactForm 
from forms import PublisherForm

def search_form(request):
    error=False
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            error=True
        else:
            books=Book.objects.filter(title__icontains=q)
            return render_to_response('books/search_results.html',
                {'books':books,'query':q}
            )
    return render_to_response('books/search_form.html',
        {'error':error}
    )
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

def add_publisher(request):
    if request.method=='POST':
        form=PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_publisher/thanks/')
        else:
            form=PublisherForm()            
        return render_to_response('books/add_publisher.html',{'form':form})