# coding=utf8
# Create your views here.

# version 1
'''
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage
def search(request):
    query = request.GET['q']
    results = FlatPage.objects.filter(content__icontains = query)
    template = loader.get_template('search/search.html')
    context = Context({ 'query': query, 'results': results })
    response = template.render(context)
    return HttpResponse(response)
'''


# version 2
'''
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage
def search(request):
    query = request.GET['q']
    return render_to_response('search/search.html',
            { 'query': query,
                'results': FlatPage.objects.filter(content__icontains = query)})
'''


# version 3
'''
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage
def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = FlatPage.objects.filter(content__icontains = query)
    return render_to_response('search/search.html',
            { 'query': query,
                'results': results })
'''

# version 4
'''
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage
def search(request):
    query = request.GET.get('q', '')
    keyword_results = []
    results = []
    if query:
        keyword_results = FlatPage.objects.filter(searchkeyword__keyword__in = query.split()).distinct() # 将简单页面中的字符串分割
        results = FlatPage.objects.filter(content__icontains = query)
    return render_to_response('search/search.html',
            { 'query': query,
                'keyword_results': keyword_results,
                'results': results })
'''

# version 5
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponseRedirect
def search(request):
    query = request.GET.get('q', '')
    keyword_results = []

    if query:
        keyword_results = FlatPage.objects.filter(searchkeyword__keyword__in = query.split()).distinct() # 将简单页面中的字符串分割
        if keyword_results.count() == 1: # 有单独结果
            return HttpResponseRedirect(keyword_results[0].get_absolute_url()) # 跳转到指定页面
        results = FlatPage.objects.filter(content__icontains = query)
    return render_to_response('search/search.html',
            { 'query': query,
                'keyword_results': keyword_results,
                'results': results })
