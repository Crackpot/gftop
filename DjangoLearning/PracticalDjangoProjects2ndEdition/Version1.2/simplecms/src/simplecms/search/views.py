#coding=utf8
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage
from django.shortcuts import render_to_response

def search(request):
    query = request.GET.get('q', '') # 取得提交的查询关键词
    keyword_results = []
    results = []
    if query:
        # 查询了东西
        keyword_results = FlatPage.objects.filter(searchkeyword__keyword__in=query.split()).distinct()
        results = FlatPage.objects.filter(content__icontains=query)
    return render_to_response('search/search.html',
                              { 'query': query,
                               'keyword_results': keyword_results,
                               'results': results })
