#coding=utf8
# Create your views here.
#crudgenerator auto-generated code.
#crudgenetaror date: 10th November 2012 23:19
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import Ziliao


class ZiliaoListView(ListView):
    model=Ziliao
    paginate_by=20

class ZiliaoDeleteView(DeleteView):
    model=Ziliao
    def get_success_url(self):
        return reverse("ziliao:ziliao:list", args=(1,))

class ZiliaoCreateView(CreateView):
    model=Ziliao
    def get_success_url(self):
        return reverse("ziliao:ziliao:list", args=(1,))

class ZiliaoUpdateView(UpdateView):
    model=Ziliao
    def get_success_url(self):
        return reverse("ziliao:ziliao:list", args=(1,))
    
#crudgenerator auto-generated code.
#crudgenetaror date: 10th November 2012 23:19
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import Jieyue


class JieyueListView(ListView):
    model=Jieyue
    paginate_by=20

class JieyueDeleteView(DeleteView):
    model=Jieyue
    def get_success_url(self):
        return reverse("ziliao:jieyue:list", args=(1,))

class JieyueCreateView(CreateView):
    model=Jieyue
    def get_success_url(self):
        return reverse("ziliao:jieyue:list", args=(1,))

class JieyueUpdateView(UpdateView):
    model=Jieyue
    def get_success_url(self):
        return reverse("ziliao:jieyue:list", args=(1,))