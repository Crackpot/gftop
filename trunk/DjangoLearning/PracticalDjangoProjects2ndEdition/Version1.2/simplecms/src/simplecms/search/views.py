#coding=utf8
from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def search(request):
    query = request.GET.get('q', '') # 取得提交的查询关键词
    keyword_results = []
    results = []
    if query:
        # 查询了东西
        keyword_results = FlatPage.objects.filter(searchkeyword__keyword__in = query.split()).distinct() # 将简单页面中的字符串分割
        if keyword_results.count() == 1: # 有唯一结果
            return HttpResponseRedirect(keyword_results[0].get_absolute_url()) # 跳转到唯一结果页面
        results = FlatPage.objects.filter(content__icontains = query)
    return render_to_response('search/search.html',
                              { 'query': query,
                               'keyword_results': keyword_results,
                               'results': results })
