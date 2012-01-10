from django import template
from django.shortcuts import get_object_or_404
from offers.models import Oferta, Categoria, Tienda
from settings import MEDIA_URL
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from offers.views import OFFERS_PER_PAGE
from django.db.models import Q

register = template.Library()

@register.inclusion_tag('offers/offers_list.html',takes_context=True)
def offers_list(context):
	offers_list = Oferta.objects.exclude(oferta_del_dia=True).order_by('-fecha_creacion','titulo')
	paginator = Paginator(offers_list,OFFERS_PER_PAGE)
	offers =  paginator.page(1)
	return { 'offers': offers,'MEDIA_URL': MEDIA_URL, "request":context['request'] } 

@register.inclusion_tag('offers/oferta_del_dia.html',takes_context=True)
def oferta_del_dia(context):
	oferta = Oferta.objects.filter(oferta_del_dia=True)[0]
	return { 'oferta':oferta,'MEDIA_URL': MEDIA_URL }

@register.inclusion_tag('offers/categories.html',takes_context=True)
def categories_list(context):
	categories = Categoria.objects.all()
	return { 'categories':categories }

@register.inclusion_tag('offers/offers_carrousel.html',takes_context=True)
def offers_carrousel(context):
	offers_list = Oferta.objects.exclude(oferta_del_dia=True).order_by('-fecha_creacion','titulo')[0:20] 
	oferta = Oferta.objects.filter(oferta_del_dia=True)[0]
	return {'offers':offers_list,'MEDIA_URL': MEDIA_URL, 'oferta':oferta, }

@register.inclusion_tag('offers/stores_list.html',takes_context=True)
def stores_list(context, category):
	stores_list = Tienda.objects.filter(Q(categoria=category))
	return {'stores_list':stores_list,'MEDIA_URL': MEDIA_URL }
