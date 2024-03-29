#coding=utf8
from django.shortcuts import render_to_response
from django.http import Http404
import datetime

def current_datetime(request):
    # 模板中使用了It is now {{ current_date }}.，在此我们可以定义同样的变量名直接通过Python的内建函数locals()来渲染页面
    current_date = datetime.datetime.now()
    return render_to_response('time/current_datetime.html', locals())

def hours_ahead(request, offset):
    try:
        #(r'^plus/(\d{1,2})/$', hours_ahead),
        #offset是前面url中带过来的参数
        hour_offset = int(offset)
    except ValueError:
        # 值为非数值型
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours = hour_offset)
    assert True
    #assert False #产生500页面
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>"%(offset, dt)
    #return HttpResponse(html)
    #return render_to_response('hours_ahead.html', {'offset': offset, 'dt': dt})
    # 模板中使用了In {{ offset }} hour(s), it will be {{ dt }}.，直接使用locals()来渲染
    return render_to_response('time/hours_ahead.html', locals())
