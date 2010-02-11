# coding=utf8
# Create your views here.

# Version 1
'''
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
'''

# Version 2
'''
from mysite.polls.models import Poll
from django.http import HttpResponse
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    output = '.'.join([p.question for p in latest_poll_list])
    return HttpResponse(output)
'''

# Version 3
'''
from django.template import Context, loader
from mysite.polls.models import Poll
from django.http import HttpResponse
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
        })
    return HttpResponse(t.render(c))
'''

# Version 4
'''
from django.shortcuts import render_to_response
from mysite.polls.models import Poll
from django.http import Http404
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html',
            {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk = poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html',
            {'poll': p})
'''

# Version 5
from django.shortcuts import render_to_response, get_object_or_404
from mysite.polls.models import Poll
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html',
            {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk = poll_id)
    return render_to_response('polls/detail.html',
            {'poll': p})
