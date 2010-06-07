#coding=utf8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from mysite.polls.models import Choice, Poll

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk = poll_id)
    try:
        selected_choice = poll.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render_to_response('polls/detail.html',{
            'poll': poll,
            'error_message': "You didn't selected a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(
        # 在构造 HttpResponseRedirect 对象时使用了 reverse() 函数。这个函数解决了在视图中硬编码 URL 问题。我们只要给出要重定向的视图的名称和这个视图需要的参数就可以了。
        reverse('mysite.polls.views.results', args=(poll.id,))
    )
