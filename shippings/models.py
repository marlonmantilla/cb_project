from django.db import models
from offers.models import Producto, Oferta
from profiles.models import Profile
from django.utils.translation import ugettext_lazy as _

class Transportadora(models.Model):
	nombre = models.CharField(_("Nombre"), blank=False, unique=True, max_length=255)
	
	def __unicode__(self):
		return self.nombre

class Envio(models.Model):
	pais = models.CharField(_("Pais"), blank=True, max_length=255)	
	ciudad = models.CharField(_("Ciudad"), blank=True, max_length=255)
	proveedor = models.CharField(_("Proveedor"), blank=True, max_length=255)
	tipo = models.CharField(_("Tipo"), blank=True, max_length=255)	
	guia = models.CharField(_("No. de guia"), blank=False, max_length=255, default="")	
	transportadora = models.ForeignKey(Transportadora, blank=True, null=True)
	productos = models.ManyToManyField(Producto, verbose_name="Productos")
	observaciones = models.TextField(_("Observaciones"), blank=True)
	estado = models.IntegerField(default=0, blank=True, null=True)
	usuario = models.ForeignKey(Profile, blank=True, null=True)
	oferta = models.ForeignKey(Oferta, blank=True, null=True)
	RESPONSABLE = {'cittybox':"Por Cittybox", 'usuario':"Por usuario"}
	comprado = models.CharField(_("Comprado por"), blank=True, null=True, default = RESPONSABLE['usuario'],max_length=255)	
	ESTADOS = {'recibido':1, 'no_recibido':0, 'en_locker': 2}
	fecha_creacion = models.DateTimeField(_("Fecha de creacion"),auto_now_add=True, blank=True, null=True) 

	def __unicode__(self):
		return self.guia

	def estado_str(self):
		if self.estado == Envio.ESTADOS['no_recibido']:
			return '<span style="color:red;">Por Recibir</span>'
		elif self.estado == Envio.ESTADOS['en_locker']:
			return '<span style="color:blue;">En bodega</span>'
		else:
			return '<span style="color:green;">Recibido</span>' 
	estado_str.allow_tags = True
	estado_str.short_description = "Estado"
		
			
