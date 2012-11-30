#coding=utf8
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from polls.models import Choice, Poll
from ziliao.models import Ziliao


def index(request):
    latest_ziliao_list = Ziliao.objects.all().order_by('-zl_cundangshijian')[:1]
    return render_to_response('ziliao/index.html', {'latest_ziliao_list': latest_ziliao_list})

## ...
#def detail(request, ziliao_id):
#    zl = get_object_or_404(Ziliao, pk=ziliao_id)
#    return render_to_response('ziliao/detail.html', {'ziliao': zl},
#                               context_instance=RequestContext(request))
#
#def results(request, poll_id):
#    p = get_object_or_404(Poll, pk=poll_id)
#    return render_to_response('polls/results.html', {'poll': p})
#
## ...
#def vote(request, poll_id):
#    p = get_object_or_404(Poll, pk=poll_id)
#    try:
#        selected_choice = p.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the poll voting form.
#        return render_to_response('polls/detail.html', {
#            'poll': p,
#            'error_message': "You didn't select a choice.",
#        }, context_instance=RequestContext(request))
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        #return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
#        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))