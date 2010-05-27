from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from tagging.models import TaggedItem
from voting.models import Vote

from mysite.items.models import Item

class ItemData:
    def __init__(self, item, score):
        self.item = item
        self.score = score

def view_item_list(request):
    items = Item.objects.all()
    # This is a temporary simple view
    # See urls.py for further information
    data = []
    for item in items:
        score = Vote.objects.get_score(item)
        data.append(ItemData(item, score))
    return render_to_response('items/item_list.html', RequestContext(request, {'data': data}))

def view_cloud(request):
    if request.method == 'POST':
        item_name = request.POST['item']
        try:
            item = Item.objects.get(name=item_name)
        except (KeyError, Item.DoesNotExist):
            item = Item(name=item_name)
            item.save()
        return HttpResponseRedirect('/items/%s'%item_name)
    tags = Item.tags.cloud()
    return render_to_response('items/cloud.html', RequestContext(request, {'tags': tags}))

def view_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        tags = request.POST['tags']
        item.tags = tags
    
    vote = None
    if request.user.is_authenticated():
        vote = Vote.objects.get_for_user(item, request.user)
    score = Vote.objects.get_score(item)
    
    return render_to_response('items/item.html', RequestContext(request, {'item': item, 'score':score, 'vote':vote}))

def view_tag(request, tag_name):
    items = TaggedItem.objects.get_by_model(Item, tag_name)
    return render_to_response('items/tag.html', RequestContext(request, {'tag_name':tag_name, 'items': items}))
