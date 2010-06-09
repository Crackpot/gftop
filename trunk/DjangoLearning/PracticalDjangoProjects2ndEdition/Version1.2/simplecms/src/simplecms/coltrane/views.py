#coding=utf8
from django.shortcuts import render_to_response
from simplecms.coltrane.models import Entry

def entries_index(request):
    return render_to_response('coltrane/entry_index.html',
                              {'entry_list': Entry.objects.all()})
def entry_detail(request):
    return render_to_response('coltrane/entry_index.html')
