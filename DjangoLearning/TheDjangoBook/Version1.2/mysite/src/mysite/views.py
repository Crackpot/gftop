#coding=utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template

def index(request):
    return render_to_response('index.html')

def hello(request):
    return HttpResponse('Hello world<br/><a href="../">return</a>')

def display_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('display_meta.html', locals())

def debug(request):
    return HttpResponse('Debuginfo')

def about_pages(request, page):
    try:
        return direct_to_template(
            request,
            template= "about/%s.html" % page
        )
    except TemplateDoesNotExist:
        raise Http404()
    
def add(request):
    if request.POST.has_key('a'):
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        c = a + b
    else:
        a = 0
        b = 0
        c = 0
    return render_to_response('add.html', locals())