from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings
from profiles.forms import SignupFormExtra
from settings import MEDIA_ROOT
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('userena.urls')),
    (r'^messages/', include('userena.contrib.umessages.urls')),
    
    url(r'^ofertas/$', 'offers.views.index', name='offers'),
    url(r'^ofertas/comprar/(?P<id_offer>[\d]+)/$', 'offers.views.shop', name='shop_offer'),
    url(r'^ofertas/(?P<store>[-\w]+)/(?P<offer_id>\d+)/$', 'offers.views.show', name='show_offer'),
    url(r'^filtrar_categoria/(?P<categoria_id>[\d]+)/$', 'offers.views.filtrar_categoria', name='filtrar_categoria'),
    url(r'^offers_list/$', 'offers.views.offers_list', name='offers_list'),
    url(r'^search/$', 'offers.views.search', name='search'),
    url(r'^add_to_favorites/(?P<offer_id>[\d]+)/$', 'offers.views.add_to_favorites', name='add_to_favorites'),
    url(r'^tiendas/$', 'offers.views.stores', name='stores'),
    url(r'^new_product/$', 'offers.views.new_product', name='new_product'),
    url(r'^delete_product/$', 'offers.views.delete_product', name='delete_product'),


    url(r'^login/$', 'profiles.views.login_user', name='login'),
    url(r'^logout/$', 'profiles.views.logout_user', name='logout'),
        
    url(r'^prealertar/$', 'shippings.views.prealertar', name='prealertar'),
    url(r'^autoshop/(?P<offer_id>[\d]+)/$', 'shippings.views.autoshop', name='autoshop'),
    url(r'^shippings/filter_by_state/$', 'shippings.views.filter_by_state', name='filter_by_state'),
    url(r'^validate_code/$', 'shippings.views.validate_code', name='validate_code'),
    
    

	url(r'^$', 'views.home', name='home'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    (r'^i18n/', include('django.conf.urls.i18n')),
    

)

