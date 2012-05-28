from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from userena.forms import AuthenticationForm
from django.core.urlresolvers import reverse


def how_it_works(request):
	return render_to_response('dashboard/how_works.html',locals(), context_instance=RequestContext(request)) 

def under_construction(request):
	return render_to_response('dashboard/construccion.html',locals(), context_instance=RequestContext(request)) 

def home(request):
	if request.user.is_authenticated():
		if request.user.username == "admin":
			return redirect("admin/") 
		else:
			return redirect("accounts/%s" % request.user)
	else:
		form = AuthenticationForm()
		return render_to_response('dashboard/home.html',{'form':form,}, context_instance=RequestContext(request)) 