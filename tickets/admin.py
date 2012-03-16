from tickets.models import Ticket
from django.contrib import admin
from email_notifications import *

 
class TicketAdmin(admin.ModelAdmin):
  list_filter = ('usuario',)
  search_fields = [ 'usuario__user__first_name', 'usuario__user__last_name', 'usuario__user__username', 'subject' ]
  #actions = ( 'received', 'no_recibido', 'en_bodega', )
    
	
  def close(self, request, queryset):
  	pass
	# envios = queryset.update(estado=Envio.ESTADOS['recibido'])
	# for envio in queryset:
	# 	send_status_notification(envio)
	# if envios == 1:
	# 	self.message_user(request, "%s marcado como recibido" % 1)
	# else:
	# 	self.message_user(request, "%s marcados como recibido" % envios)
  close.short_description = 'Recibido(s).'

admin.site.register(Ticket, TicketAdmin)



	
  


