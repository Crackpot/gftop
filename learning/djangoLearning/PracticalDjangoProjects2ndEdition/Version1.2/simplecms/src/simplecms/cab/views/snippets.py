#coding=utf8
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.forms import ModelForm, Textarea
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from simplecms.cab.models import Snippet

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        exclude = ['author']
        widgets = {'code': Textarea(attrs={'cols': 80, 'rows': 10})}

        
def add_snippet(request):
    if request.method == 'POST':
        form = SnippetForm(data = request.POST)
        if form.is_valid():
            new_snippet = form.save(commit = False)
            new_snippet.author = request.user
            new_snippet.save()
            return HttpResponseRedirect(new_snippet.get_absolute_url())
    else:
        form = SnippetForm()
    return render_to_response('cab/snippet_form.html',
                              {'form': form, 'add': True})
add_snippet = login_required(add_snippet)


def edit_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk = snippet_id)
    if request.user.id != snippet.author.id:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = SnippetForm(instance = snippet, data = request.POST)
        if form.is_valid():
            snippet = form.save()
            return HttpResponseRedirect(snippet.get_absolute_url())
    else:
        form = SnippetForm(instance = snippet)
    return render_to_response('cab/snippet_form.html',
                                  {'form': form, 'add': False})
edit_snippet = login_required(edit_snippet)