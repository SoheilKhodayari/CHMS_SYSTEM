from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def firstpage(request):
    c={}
    c.update(csrf(request))
    return render_to_response('firstpage.html',c,context_instance=RequestContext(request))
