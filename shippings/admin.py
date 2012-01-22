from django.contrib import admin
from shippings.models import Envio, Transportadora
from django.utils.translation import ugettext_lazy as _
from email_notifications import *
 
class EnvioAdmin(admin.ModelAdmin):
  list_display = ('id','guia', 'transportadora' ,'usuario','comprado','oferta', 'estado_str', 'fecha_creacion', )
  list_display_links = ('usuario', 'guia','id')
  list_filter = ('transportadora','usuario',)
  search_fields = [ 'guia','oferta__titulo','usuario__user__username', 'usuario__user__first_name', 'usuario__user__last_name' ]
  actions = ( 'received', 'no_recibido', 'en_bodega', )
    
	
  def received(self, request, queryset):
	envios = queryset.update(estado=Envio.ESTADOS['recibido'])
	if envios == 1:
		self.message_user(request, "%s marcado como recibido" % 1)
	else:
		self.message_user(request, "%s marcados como recibido" % envios)
  received.short_description = 'Marcar como recibido(s).'
	
  def no_recibido(self, request, queryset):
	envios = queryset.update(estado=Envio.ESTADOS['no_recibido'])
	if envios == 1:
		self.message_user(request, "%s marcado como NO recibido" % 1)
	else:
		self.message_user(request, "%s marcados como NO recibido" % envios)
  no_recibido.short_description = 'Marcar como NO recibido(s).'

  def en_bodega(self, request, queryset):
	envios = queryset.update(estado=Envio.ESTADOS['en_locker'])
	if envios == 1:
		self.message_user(request, "%s marcado en bodega" % 1)
	else:
		self.message_user(request, "%s marcados en bodega" % envios)
  en_bodega.short_description = 'Marcar como paquete(s) en bodega.'



admin.site.register(Envio, EnvioAdmin)
admin.site.register(Transportadora)