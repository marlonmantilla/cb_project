from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from tickets.forms import TicketForm
from email_notifications import *
from django.contrib import messages


def index(request):
	return render_to_response('tickets/index.html', locals() , context_instance=RequestContext(request))

def add(request):

	if request.method == 'POST':
		form = TicketForm(request.POST)
		if form.is_valid():
			form.save(commit=False)
			if request.user.is_authenticated():
				form.usuario = request.user.get_profile()
			form.save()
			messages.add_message(request, messages.INFO, 'Su pregunta ha sido enviada correctamente.')
	else:
		form = TicketForm()
			
	return render_to_response('tickets/new.html', locals() , context_instance=RequestContext(request))