from django import template
from django.shortcuts import get_object_or_404
from shippings.models import Envio

register = template.Library()

@register.inclusion_tag('shippings/shippings_list.html')
def shippings_list(user):
	shippings = Envio.objects.filter(usuario=user)
	return { 'shippings': shippings, } 