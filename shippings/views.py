from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from shippings.forms import PrealertForm
from shippings.models import Envio
from offers.models import Oferta
from django.http import HttpResponse
from django.utils import simplejson
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import get_template
from django.template import Context
from settings import MEDIA_URL

SHIPPINS_PER_PAGE = 2


def filter_by_state(request):
	if request.POST:
		state = request.POST.get('state')
		envios_list = Envio.objects.filter(usuario=user)	

def validate_code(request):
	code = request.GET.get("code")
	try:
		Envio.objects.get(guia=code)
		return HttpResponse("ERROR")
	except ObjectDoesNotExist:
		return HttpResponse("OK")


def autoshop(request, offer_id):
	offer = Oferta.objects.get(pk=offer_id)
	if request.method == 'POST':
		envio = Envio(usuario=request.user.get_profile(), comprado=Envio.RESPONSABLE['cittybox'],oferta=offer)
		envio.save()
		productos = offer.productos.iterator()
		for producto in productos:
			envio.productos.add(producto)
		envio.save()
		success = True
	
	return render_to_response('shippings/autoshop.html', locals() , context_instance=RequestContext(request))

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
			envio.comprado = Envio.RESPONSABLE['usuario']
			envio.save()
			productos = form.cleaned_data['productos']
			
			for producto in productos:
				envio.productos.add(producto)
				
			envio.save()
			htmly     = get_template('emails/test.html')
			d = Context({ 'user': request.user, 'MEDIA_URL': MEDIA_URL, 'envio': envio })
			html_content = htmly.render(d)
			subject, from_email, to = 'Paquete prealertado en Cittybox', 'no-reply@cittybox.com', request.user.email
			msg = EmailMessage(subject, html_content, from_email, [to])
			msg.content_subtype = "html"
			msg.send()
			return redirect("/accounts/%s" % request.user)
	else:
		form = PrealertForm()
		
	
	return render_to_response('shippings/prealertar.html',{'form': form,}, context_instance=RequestContext(request)) 