#coding=utf8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from mysite.books import forms
from mysite.books.models import Book, Publisher, Author

def index(request):
    return render_to_response("index_books.html")

def book_detail(request, id):
    book = Book.objects.get(id = id)
    authors = Book.get_authors(book)
    print book
    print authors
    return render_to_response(
        'detail_book.html',
        {'book': book, 'authors':authors}
    )
def publisher_detail(request, id):
    publisher = Publisher.objects.get(id = id)
    return render_to_response(
        'detail_publisher.html',
        {'publisher': publisher,}
    )
    
def bookEdit(request, id): # 传来的参数id在Url中已经定义了类型
    book = Book.objects.get(id = id)
    if request.method == 'POST':
        # 已经提交表单
        form = forms.BookForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
    else:
        # 未提交表单
        form = forms.BookForm(instance = book)
        return render_to_response(
            'form_book.html',
            {'form': form},
        )
    return HttpResponseRedirect('/books/books/%s/' % id) # 返回之前的图书详情页面
def publisherEdit(request, id):
    publisher = Publisher.objects.get(id = id)
    if request.method == 'POST':
        #已经提交表单
        form = forms.PublisherForm(request.POST, instance = publisher)
        if form.is_valid():
            form.save()
    else:
        # 未提交表单
        form = forms.PublisherForm(instance = publisher)
        return render_to_response(
            'form_publisher.html',
            {'form': form},
        )
def search(request):
    # 一个视图方法渲染不同页面的实例
    errors = []
    # http://127.0.0.1:8000/books/search?q=人
    if 'q' in request.GET: # request.GET是个字典
        """
        取得q之后去掉前后空格时成为列表，需要取出第一个值，否则会出现[u'\u4eba']之类的东西
        """
        q = request.GET['q'].strip() # 在此去掉空格
        if not q:
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
