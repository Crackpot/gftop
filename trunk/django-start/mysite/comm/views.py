from django.contrib.comments.views.comments import post_comment
from django.http import HttpResponseRedirect

def redirect_post_comment(request):
    if request.REQUEST.has_key('target_url') and not request.REQUEST.has_key('preview'):
        response = post_comment(request)
        
        # Check there's a url to redirect to, and that post_free_comment worked
        if len(request.REQUEST['target_url'].strip()) > 0 and isinstance(response, HttpResponseRedirect):
            return HttpResponseRedirect(request.REQUEST['target_url'])
        
        # Fall back on the default post_free_comment response
        return response
    
    return post_comment(request)
