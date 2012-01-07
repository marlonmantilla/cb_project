from django import template
from django.shortcuts import get_object_or_404
from offers.models import Oferta
from settings import MEDIA_URL
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from offers.views import OFFERS_PER_PAGE
register = template.Library()

@register.inclusion_tag('offers/offers_list.html')
def offers_list():
	offers_list = Oferta.objects.exclude(oferta_del_dia=True).order_by('fecha_creacion','titulo')
	paginator = Paginator(offers_list,OFFERS_PER_PAGE)
	offers =  paginator.page(1)
	return { 'offers': offers,'MEDIA_URL': MEDIA_URL } 