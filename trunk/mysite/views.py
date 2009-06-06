#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response 
import datetime

def index(request):
    return HttpResponse("主页  您所在的位置为：%s"%(request.path).encode('utf-8'))
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
def foo_view(request):
    return HttpResponse('<h1>foo</h1>')
def bar_view(request):
    return HttpResponse('<h1>bar</h1>')