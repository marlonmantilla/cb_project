from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from offers.models import Oferta, Categoria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import operator

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


def search_keywords(keywords):
    
    if isinstance(keywords, str):
        keywords = [keywords]

    if not isinstance(keywords, list):
        return None

    list_body_qs = [Q(titulo__icontains=x) for x in keywords]
    list_subj_qs = [Q(descripcion__icontains=x) for x in keywords]
    final_q = reduce(operator.and_, list_body_qs + list_subj_qs)
    r_qs = Oferta.objects.filter(final_q)
    return r_qs

def search(request):
 	offers_list = search_keywords(['kindle','fire'])
 	q = request.GET.get('q')
 	print q
 	paginator = Paginator(offers_list,OFFERS_PER_PAGE)
 	offers = paginator.page(1)
 	return render_to_response('offers/offers_list.html', {'offers':offers}, context_instance=RequestContext(request))
