from django import template
from django.shortcuts import get_object_or_404
from shippings.models import Envio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from offers.models import Oferta, Favoritas

register = template.Library()

SHIPPINGS_PER_PAGE = 5

@register.inclusion_tag('shippings/filter.html', takes_context=True)
def shippings_filter(context):
	return { 'states': Envio.ESTADOS }	

@register.inclusion_tag('shippings/ofertas_favoritas.html')
def ofertas_favoritas(user):
	offers = Favoritas.objects.filter(usuario=user.get_profile())
	return { 'offers': offers, } 

@register.inclusion_tag('shippings/shippings_list.html', takes_context=True)
def shippings_list(context, user):
	request = context["request"]
	shippings_list = Envio.objects.filter(usuario=user).order_by('estado')
	paginator = Paginator(shippings_list,SHIPPINGS_PER_PAGE)
	if request.GET.get('page') != None:
		page = request.GET.get('page')
	else:
		page = 1
	try:
		shippings = paginator.page(page)
	except PageNotAnInteger:
		shippings = paginator.page(1)
	except EmptyPage:
		shippings = paginator.page(paginator.num_pages)
	return { 'shippings': shippings, } 