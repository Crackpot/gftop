#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response 
import datetime

def index(request):
    return render_to_response('index.html')
def hello(request):
    return HttpResponse("您好！ 您所在的位置为：%s"%(request.path).encode('utf-8'))
def checkbrowser(request):
    ua=request.META.get('HTTP_USER_AGENT','不明')
    return  HttpResponse('您的浏览器类型为：<BR>%s'%ua)
def display_meta(request):
    values=request.META.items()
    values.sort()
    html=[]
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>'%'\n'.join(html))
def current_datetime(request):
    current_date=datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())
def hours_ahead(request,offset):
    hour_offset=int(offset)
    next_time=datetime.datetime.now()+datetime.timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html',locals())
def now_in_london(request):
    #伦敦在0时区
    city='伦敦'
    hour_offset=-7
    time_london=datetime.datetime.now()+datetime.timedelta(hours=hour_offset)
    return HttpResponse('<head><title>伦敦时间</title></head><body><h1>伦敦当前时间为：%s</h1></body>'%time_london)
def foo_view(request):
    return HttpResponse('<h1>foo</h1>')
def bar_view(request):
    return HttpResponse('<h1>bar</h1>')
def say_hello(request,person_name):
    return HttpResponse('Hello, %s'%person_name)
def say_goodbye(request,person_name):
    return HttpResponse('Goodbye,%s'%person_name)
from django.template import loader,RequestContext
def custom_proc(request):
    return {
        'app':'My app',
        'user':request.user,
        'ip_address':request.META['REMOTE_ADDR']
    }
def view_1(request):
    t = loader.get_template('template1.html')
    c = RequestContext(request, {'message': 'I am view 1.'},
            processors=[custom_proc])
    return t.render(c)

