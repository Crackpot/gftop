#coding=utf8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from simplecms.forms import SignupForm

def index(request):
    return render_to_response('index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = SignupForm()
    return render_to_response('signup.html',
                             {'form': form})
