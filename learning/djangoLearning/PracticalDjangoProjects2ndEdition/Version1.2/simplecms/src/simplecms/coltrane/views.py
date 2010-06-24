#coding=utf8
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.list_detail import object_list
from simplecms.coltrane.models import Entry, Category

def category_detail(request, slug):
    category = get_object_or_404(Category, slug = slug)
    return render_to_response('coltrane/category_detail.html',
                              {'object_list': category.live_entry_set(),
                               'slug': slug })
"""
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    queryset = category.entry_set.all()
    # 在entry模型总，categories = models.ManyToManyField(Category)
    # 渲染category_list.html
    return object_list(request,
                       queryset,
                       extra_context={'category': category,
                                        'slug': slug, })
"""
    
# 下面的两个方法都被通用视图所替代
def entries_index(request):
    return render_to_response('coltrane/entry_index.html',
            {'entry_list': Entry.objects.all()})

def entry_detail(request, year, month, day, slug):
    import datetime, time
    date_stamp = time.strptime(year + month + day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    entry = get_object_or_404(Entry, pub_date__year = pub_date.year,
                              pub_date__month = pub_date.month,
                              pub_date__day = pub_date.day,
                              slug=slug)
    return render_to_response('coltrane/entry_detail.html',
                              { 'entry': entry })
"""
    return render_to_response('coltrane/entry_detail.html',
                              {'entry': Entry.objects.get(pub_date__year = pub_date.year,
                                                          pub_date__month = pub_date.month,
                                                          pub_date__day = pub_date.day,
                                                          slug = slug)})

"""
