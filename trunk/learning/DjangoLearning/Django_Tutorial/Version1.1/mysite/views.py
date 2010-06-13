# coding=utf8
from django.shortcuts import render_to_response

# 页面不存在
def my_custom_404_view(request):
    return render_to_response('404.html')

# 服务器错误
def my_custom_error_view(request):
    return render_to_response('500.html')
