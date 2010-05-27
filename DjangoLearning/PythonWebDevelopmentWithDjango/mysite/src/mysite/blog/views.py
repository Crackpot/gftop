#coding=utf8
from django.shortcuts import render_to_response
from mysite.blog.models import BlogPost
def archive(request):
    posts = BlogPost.objects.all()
    return render_to_response(
        'archive.html', {'posts':posts}
    )
