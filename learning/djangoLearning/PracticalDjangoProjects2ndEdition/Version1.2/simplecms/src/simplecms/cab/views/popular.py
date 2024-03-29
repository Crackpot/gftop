#coding=utf8
from django.views.generic.list_detail import object_list
from simplecms.cab.models import Language, Snippet
from django.contrib.auth.models import User
from django.db.models import Count

def top_authors(request):
    return object_list(request, queryset = Snippet.objects.top_authors(),
                       template_name = 'cab/top_authors.html',
                       paginate_by = 20)

def top_languages(request):
    return object_list(request,
                       queryset = Language.objects.top_languages(),
                       template_name = 'cab/top_languages.html',
                       paginate_by = 20)
    
def most_bookmarked(request):
    return object_list(queryset = Snippet.objects.most_bookmarked(),
                       template_name = 'cab/most_bookmarked.html',
                       paginate_by = 20)
"""
User.objects.annotate(score = Count('snippet')).order_by('score')

def top_authors(request):
    top_authors_qs = User.objects.annotate(score = Count('snippet')).order_by('score')
    return object_list(request, queryset = top_authors_qs,
                       template_name = 'cab/top_authors.html',
                       paginate_by = 20)
"""
