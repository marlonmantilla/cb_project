from django.contrib import admin
from shippings.models import Envio, Transportadora
from django.utils.translation import ugettext_lazy as _
 
class EnvioAdmin(admin.ModelAdmin):
  list_display = ('id','guia', 'transportadora' ,'usuario', 'estado_str', )
  list_display_links = ('usuario', 'guia','id')
  list_filter = ('transportadora',)
  search_fields = [ 'guia',]
  actions = ( 'received', 'no_recibido', )
    
	
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



admin.site.register(Envio, EnvioAdmin)
admin.site.register(Transportadora)