from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from offers.models import Oferta, Categoria, Favoritas, Tienda, Producto
from offers.forms import ProductForm
from shippings.models import Envio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
import operator

OFFERS_PER_PAGE = 12

def index(request):
	oferta_del_dia = get_object_or_404(Oferta, oferta_del_dia=True)
	categorias = Categoria.objects.all().order_by('nombre')
	prealertados = Envio.objects.filter(oferta=oferta_del_dia).count
	favoritas = Favoritas.objects.filter(oferta=oferta_del_dia).count
	
	return render_to_response('offers/index.html', {'main_offer':oferta_del_dia, 
	'categorias': categorias,'prealertados':prealertados, 'favoritas':favoritas }, context_instance=RequestContext(request)) 

def delete_product(request):
	if request.POST:
		product_id = request.POST["product_id"]
		Producto.objects.get(pk=product_id).delete()
		return HttpResponse("OK")

def shop(request, id_offer):
	offer = Oferta.objects.get(pk=id_offer)
	return render_to_response('offers/shop.html', {'offer':offer}, context_instance=RequestContext(request)) 

def show(request, store, offer_id):
	try:
		offer = Oferta.objects.get(pk=offer_id, activa=True)
		tienda = Tienda.objects.get(nombre__iexact=store)
	except ObjectDoesNotExist:
		raise Http404
	prealertados = Envio.objects.filter(oferta=offer).count
	favoritas = Favoritas.objects.filter(oferta=offer).count
	categorias = Categoria.objects.all().order_by('nombre')
	en_envio = None
	if not request.user.is_anonymous and request.user.is_authenticated:
		en_envio = Envio.objects.filter(oferta=offer, usuario=request.user.get_profile(), estado=Envio.ESTADOS['no_recibido'])

	return render_to_response('offers/show.html', {'en_envio':en_envio,'main_offer':offer, 
	'prealertados': prealertados,'categorias': categorias, 'tienda':tienda, 'favoritas':favoritas }, context_instance=RequestContext(request)) 

def new_product(request):
	if request.method == "POST":

		if 'product_id' in request.POST:
			id = request.POST['product_id']
			producto = Producto.objects.get(pk=id)
			form = ProductForm(request.POST, instance=producto)
		else:
			form = ProductForm(request.POST)
		
		if form.is_valid():
			
			if 'product_id' in request.POST:
				producto.save()
				return render_to_response('offers/new_product.html', 
				{'form':form, 'product_id':id }, context_instance=RequestContext(request))				
			else:
				producto = form.save(commit=False)
				producto.usuario = request.user.get_profile()
				producto.save()
				return render_to_response('offers/new_product.html', 
				{'form':form, 'product_id':producto.id }, context_instance=RequestContext(request))

		else:
			return HttpResponse("ERROR")
	else:
		form = ProductForm()

	return render_to_response('offers/new_product.html', {'form':form }, context_instance=RequestContext(request))

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
	offers_list = Oferta.objects.exclude(oferta_del_dia=True).order_by('-fecha_creacion','titulo')
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
    final_q = reduce(operator.and_, list_body_qs + list_subj_qs )
    r_qs = Oferta.objects.filter(final_q)
    return r_qs

def search(request):
 	q = request.GET.get('q').split('+')
 	offers_list = search_keywords(q)
 	paginator = Paginator(offers_list,OFFERS_PER_PAGE)
 	offers = paginator.page(1)
 	return render_to_response('offers/offers_list.html', {'offers':offers}, context_instance=RequestContext(request))

def add_to_favorites(request, offer_id):
	oferta = Oferta.objects.get(id=offer_id)
	favorita = Favoritas(oferta=oferta,usuario=request.user.get_profile() )
	print oferta
	print favorita
	print favorita.save()
	return HttpResponse("OK")

def stores(request):
	stores = Tienda.objects.all()
	categories = Categoria.objects.all().order_by('nombre')
	return render_to_response('offers/stores.html',{'stores':stores, 'categories':categories}, context_instance=RequestContext(request))