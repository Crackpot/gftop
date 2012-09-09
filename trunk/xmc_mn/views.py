#coding=utf8

from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response
from mezzanine.blog.models import BlogPost
import datetime

def hello(request):
    return HttpResponse("hello")

def home(request):
    blog_posts = BlogPost.objects.published()[:5]
    #print blog_posts
    request.path = "/"
    template = "index.html"
    context = {"blog_posts":blog_posts}
    return render(request, template, context)