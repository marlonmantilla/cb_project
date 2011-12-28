from django.db import models
from profiles.models import Profile
from django.utils.translation import ugettext_lazy as _

class Categoria(models.Model):
    nombre = models.CharField(_("Nombre"), blank=False, unique=True, max_length=255)
    categoria = models.ForeignKey('self', related_name="main_category", blank=True, default=None,null=True)

    def __unicode__(self):
		return self.nombre

class Tienda(models.Model):
    nombre = models.CharField(_("Nombre"), blank=False, unique=True, max_length=255)
    url = models.URLField(_('Url'), blank=True, verify_exists=True)
    categoria = models.ForeignKey(Categoria)

    def __unicode__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(_("Nombre"), blank=False, unique=True, max_length=255)
	cantidad = models.CharField(_("Cantidad"), blank=False, unique=True, max_length=255)
	valor = models.CharField(_("Valor"), blank=False, unique=True, max_length=255)
	
	def __unicode__(self):
		return self.nombre

class Oferta(models.Model):
	titulo = models.CharField(_("Titulo"),max_length=255, blank=False)
	descripcion = models.TextField(_('Descripcion'), blank=False )
	precio = models.CharField( _("Precio"), blank=False, max_length=30 )
	precio_anterior = models.CharField(_("Precio Anterior"), blank=False, max_length=30)
	productos = models.ManyToManyField(Producto, verbose_name="Products")
	tienda = models.ForeignKey(Tienda)
	imagen = models.ImageField(upload_to='media/mugshots/')
	
	def __unicode__(self):
		return self.titulo

class Favoritas(models.Model):
	oferta = models.ForeignKey(Oferta)
	usuario = models.ForeignKey(Profile)
	
	def __unicode__(self):
		return self.oferta.titulo
		