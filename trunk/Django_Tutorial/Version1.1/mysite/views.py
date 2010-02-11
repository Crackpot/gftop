# coding=utf8
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world!")

def my_custom_404_view(request):
    return HttpResponse("my_custom_404_view")

def my_custom_error_view(request):
    return HttpResponse("my_custom_error_view")
