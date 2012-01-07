from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from offers.models import Oferta, Categoria

def index(request):
	oferta_del_dia = get_object_or_404(Oferta, oferta_del_dia=True)
	categorias = Categoria.objects.all().order_by('nombre')
	return render_to_response('offers/index.html', {'main_offer':oferta_del_dia, 
	'categorias': categorias, }, context_instance=RequestContext(request)) 


def filtrar_categoria(request, id_categoria):
	offers = Oferta.objects.filter(categoria=id_categoria)
	return render_to_response('offers/offers_list.html',{'offers':offers}, context_instance=RequestContext(request))