from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.utils import simplejson

def logout_user(request):
	logout(request)
	return redirect("/")

def login_user(request):
	if request.POST:
		username = request.POST.get('identification')
		password = request.POST.get('password')
		print username
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You're successfully logged in!"
				status = 200
			else:
				state = "Su cuenta se encuentra inactiva, contacte al administrador"
				state = 400
		else:
			state = "Combinaci&oacute;n de Nombre de Usuario err&oacute;nea"
			status = 400
	to_json = { "message": state, "status": status }			
	return HttpResponse(simplejson.dumps(to_json), mimetype="application/json")