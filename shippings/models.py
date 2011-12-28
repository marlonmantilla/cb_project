from django.db import models
from offers.models import Producto
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
	guia = models.CharField(_("No. de guia"), blank=True, unique=True, max_length=255)	
	transportadora = models.ForeignKey(Transportadora, unique=True)
	productos = models.ManyToManyField(Producto, verbose_name="Productos")
	observaciones = models.TextField(_("Observaciones"))
	estado = models.IntegerField()
	usuario = models.ForeignKey(Profile, blank=False)
	
	def __unicode__(self):
		return self.guia
			
