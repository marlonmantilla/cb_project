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
    
    url(r'^offers/$', 'offers.views.index', name='offers'),
    url(r'^filtrar_categoria/(?P<categoria_id>[\d]+)/$', 'offers.views.filtrar_categoria', name='filtrar_categoria'),
    url(r'^offers_list/$', 'offers.views.offers_list', name='offers_list'),

    url(r'^prealertar/$', 'shippings.views.prealertar', name='prealertar'),
	url(r'^$', 'views.home', name='home'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT }),
    (r'^i18n/', include('django.conf.urls.i18n')),
    

)

