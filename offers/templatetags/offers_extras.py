from django import template
from django.shortcuts import get_object_or_404
from offers.models import Oferta
from settings import MEDIA_URL
register = template.Library()

@register.inclusion_tag('offers/offers_list.html')
def offers_list():
	offers = Oferta.objects.exclude(oferta_del_dia=True).order_by('titulo')
	return { 'offers': offers,'MEDIA_URL': MEDIA_URL } 