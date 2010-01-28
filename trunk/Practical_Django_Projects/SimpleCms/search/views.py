# coding=utf8

# Create your views here.

from django.shortcuts import render_to_response # 改进，引入快捷方式
from django.contrib.flatpages.models import FlatPage

def search(request):
    # 访问地址如： http://www.example.com/search?q=foo
    query = request.GET.get('q', '') # 取出值，默认为空
    results = [] # 结果默认为空
    if query:
        results = FlatPage.objects.filter(content__icontains = query) # 查询非空则获得渲染结果
    return render_to_response('search/search.html',{
        'query': query,
        'results': results
        }) # 渲染过程中的两个参数：1。被渲染的页面地址 2。需要填充的内容
