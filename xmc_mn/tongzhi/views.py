#coding=utf8
from mezzanine.pages.views import render
from polls.models import Poll
from tongzhi.models import Tongzhi

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    latest_tongzhi_list = Tongzhi.objects.all()[:5]
    return render('index.html',
        {
         'latest_poll_list': latest_poll_list,
         'latest_tongzhi_list': latest_tongzhi_list,
         })