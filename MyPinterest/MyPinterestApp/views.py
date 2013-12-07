from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
    return render_to_response('../User/templates/homepage.html', context_instance=RequestContext(request))

def userpage(request):
    return render_to_response('../User/templates/homepage.html', context_instance=RequestContext(request))
