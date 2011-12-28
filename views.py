from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
	return render_to_response('dashboard/home.html',{}, context_instance=RequestContext(request)) 