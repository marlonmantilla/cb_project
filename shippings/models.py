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
	guia = models.CharField(_("No. de guia"), blank=False, unique=True, max_length=255)	
	transportadora = models.ForeignKey(Transportadora)
	productos = models.ManyToManyField(Producto, verbose_name="Productos")
	observaciones = models.TextField(_("Observaciones"), blank=True)
	estado = models.IntegerField(default=0, blank=True, null=True)
	usuario = models.ForeignKey(Profile, blank=True, null=True)
	oferta = models.ForeignKey(Oferta, blank=True, null=True)
	ESTADOS = {'recibido':1, 'no_recibido':0}
	
	def __unicode__(self):
		return self.guia

	def estado_str(self):
		if self.estado == Envio.ESTADOS['no_recibido']:
			return '<span style="color:red;">Por Recibir</span>'
		else:
			return '<span style="color:green;">Recibido</span>'
	estado_str.allow_tags = True
	estado_str.short_description = "Estado"
		
			
