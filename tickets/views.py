from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from email_notifications import *


def index(request):
	return render_to_response('tickets/index.html', locals() , context_instance=RequestContext(request))
