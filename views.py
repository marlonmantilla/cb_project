from django.shortcuts import render_to_response
from django.template.context import RequestContext
from userena.forms import AuthenticationForm

def home(request):
	form = AuthenticationForm()
	return render_to_response('dashboard/home.html',{'form':form,}, context_instance=RequestContext(request)) 