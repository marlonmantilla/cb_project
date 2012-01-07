from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from offers.models import Oferta, Categoria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

OFFERS_PER_PAGE = 10

def index(request):
	oferta_del_dia = get_object_or_404(Oferta, oferta_del_dia=True)
	categorias = Categoria.objects.all().order_by('nombre')
	return render_to_response('offers/index.html', {'main_offer':oferta_del_dia, 
	'categorias': categorias, }, context_instance=RequestContext(request)) 


def filtrar_categoria(request, categoria_id):
	offers_list = Oferta.objects.filter(categoria=categoria_id)
	paginator = Paginator(offers_list,OFFERS_PER_PAGE)
	# offers = paginator.page(1)
	page = request.GET.get('page')
	try:
		offers = paginator.page(page)
	except PageNotAnInteger:
		offers = paginator.page(1)
	except EmptyPage:
		offers = paginator.page(paginator.num_pages)
	return render_to_response('offers/offers_list.html',{'offers':offers, 'by_cat':True,}, context_instance=RequestContext(request))

def offers_list(request):
	offers_list = Oferta.objects.exclude(oferta_del_dia=True).order_by('fecha_creacion','titulo')
	paginator = Paginator(offers_list, OFFERS_PER_PAGE) 
	page = request.GET.get('page')
	try:
		offers = paginator.page(page)
	except PageNotAnInteger:
		offers = paginator.page(1)
	except EmptyPage:
		offers = paginator.page(paginator.num_pages)
	return render_to_response('offers/offers_list.html', {'offers':offers}, context_instance=RequestContext(request))