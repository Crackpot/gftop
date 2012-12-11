#coding=utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mezzanine.conf import settings
from mezzanine.pages import page_processors
from polls.models import Poll
from tongzhi.models import Tongzhi
from mezzanine.pages.views import render
page_processors.autodiscover()

#
#def index(request):
#    return render_to_response('index.html')


def index(request, template="index.html"):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    latest_tongzhi_list = Tongzhi.objects.all()[:5]
    context = {"latest_poll_list": latest_poll_list, "latest_tongzhi_list": latest_tongzhi_list}
    return render(request, template, context)
