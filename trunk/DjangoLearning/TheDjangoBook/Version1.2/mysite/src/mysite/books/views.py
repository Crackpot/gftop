#coding=utf8
from django.shortcuts import render_to_response
from mysite.books.models import Book

def search(request):
    # 一个视图方法渲染不同页面的实例
    errors = []
    # http://127.0.0.1:8000/books/search?q=人
    if 'q' in request.GET: # request.GET是个字典
        """
        取得q之后去掉前后空格时成为列表，需要取出第一个值，否则会出现[u'\u4eba']之类的东西
        """
        q = request.GET['q']
        if not q.split(): # 在此去掉空格
            # q为空
            errors.append('Enter a search term.')
        elif len(q) > 20:
            # 检索长度大于20
            errors.append('Please enter at most 20 characters.')
        else:
            # q非空
            books = Book.objects.filter(title__icontains = q) # 标题中包含有q
            return render_to_response(
                'search_results.html',
                {'books': books, 'query': q}
            )
    return render_to_response(
        'search_form.html',
        {'errors': errors}
    )
