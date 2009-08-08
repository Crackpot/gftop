from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list
from mysite.items.models import Item
from voting.views import vote_on_object

""" Django-Voting
This would be a much better solution:

(r'^$', object_list, dict(queryset=Item.objects.all(),
     template_object_name='item', template_name='items/item_list.html',
     paginate_by=15, allow_empty=True)),

{% load voting_tags %}
{% votes_by_user user on item_list as vote_dict %}
{% scores_for_objects item_list as score_dict %}

{% for item in item_list %}
  {% dict_entry_for_item item from vote_dict  as vote %}
  {% dict_entry_for_item item from score_dict as score %}

The dict entry for item returns a null value ?!?
"""

urlpatterns = patterns('mysite.items.views',
    (r'^$', 'view_item_list'),
    
    (r'^(?P<object_id>\d+)/(?P<direction>up|down|clear)_vote/?$',
        vote_on_object, dict(model=Item, template_object_name='item',
            template_name='items/item_confirm_vote.html',
            allow_xmlhttprequest=True)),
    
    (r'^cloud/?$','view_cloud'),
    url(r'^(?P<item_id>\d+)/$','view_item', name='items_view_item'),
    (r'^tags/(?P<tag_name>[^/]+)/$','view_tag'),
)
