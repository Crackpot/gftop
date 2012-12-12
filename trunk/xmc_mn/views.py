#coding=utf8
from mezzanine.blog.models import BlogPost
from mezzanine.pages.views import render
from polls.models import Poll
from tongzhi.models import Tongzhi

def index(request, template="index.html"):
    latest_blog_list= BlogPost.objects.all()[:5]
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    latest_tongzhi_list = Tongzhi.objects.all().order_by('-fabushijian')[:5]
    context = {
        "latest_blog_list": latest_blog_list,
        "latest_poll_list": latest_poll_list,
        "latest_tongzhi_list": latest_tongzhi_list
    }
    return render(request, template, context)
