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