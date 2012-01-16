from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from shippings.forms import PrealertForm
from django.http import HttpResponse
from django.utils import simplejson

SHIPPINS_PER_PAGE = 2

def envios_list(request):
	envios_list = Envio.objects.filter(usuario=user)
	paginator = Paginator(envios_list, SHIPPINS_PER_PAGE) 
	page = request.GET.get('page')
	try:
		envios = paginator.page(page)
	except PageNotAnInteger, EmptyPage:
		envios = paginator.page(1)
	
	return render_to_response('shippings/envios_list.html', {'shippings':envios}, context_instance=RequestContext(request))

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