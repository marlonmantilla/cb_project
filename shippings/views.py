from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from shippings.forms import PrealertForm
from django.http import HttpResponse
from django.utils import simplejson

def prealertar(request):

	if request.method == 'POST':
		form = PrealertForm(request.POST)
		
		if form.is_valid():
			envio = form.save(commit=False)
			envio.usuario = request.user.get_profile()
			envio.save()
			productos = form.cleaned_data['productos']
			
			for producto in productos:
				envio.productos.add(producto)
				
			envio.save()
			return redirect("/accounts/%s" % request.user)
	else:
		form = PrealertForm()
		
	
	return render_to_response('shippings/prealertar.html',{'form': form,}, context_instance=RequestContext(request)) 