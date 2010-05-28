#coding=utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello world")

def display_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('display_meta.html', locals())