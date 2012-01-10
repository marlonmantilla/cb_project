from django.db import models
from profiles.models import Profile
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

class Categoria(models.Model):
    nombre = models.CharField(_("Nombre"), blank=False, unique=True, max_length=255)
    categoria = models.ForeignKey('self', related_name="main_category", blank=True, default=None,null=True)

    def __unicode__(self):
		return self.nombre

class Tienda(models.Model):
    nombre = models.CharField(_("Nombre"), blank=False, unique=True, max_length=255)
    url = models.URLField(_('Url'), blank=True)
    categoria = models.ForeignKey(Categoria)
    imagen = models.ImageField(upload_to='media/stores/', blank=True, null=True)
    def __unicode__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(_("Nombre"), blank=False, max_length=255)
	cantidad = models.IntegerField(_("Cantidad"),default=1, blank=True)
	valor = models.CharField(_("Valor"), blank=False, max_length=255)
	usuario = models.ForeignKey(Profile, blank=True, null=True)
	def __unicode__(self):
		return self.nombre

class Oferta(models.Model):
	titulo = models.CharField(_("Titulo"),max_length=255, blank=False)
	descripcion = models.TextField(_('Descripcion'), blank=False )
	precio = models.CharField( _("Precio"), blank=False, max_length=30 )
	precio_anterior = models.CharField(_("Precio Anterior"), blank=True, max_length=30)
	productos = models.ManyToManyField(Producto, blank=True, verbose_name="Products")
	tienda = models.ForeignKey(Tienda, blank=True)
	imagen = models.ImageField(upload_to='media/mugshots/')
	oferta_del_dia = models.BooleanField(blank=True,default=False)
	url = models.URLField(blank=True) 
	categoria = models.ForeignKey(Categoria, blank=True, null=True)
	fecha_creacion = models.DateTimeField(_("Fecha de creacion"),auto_now_add=True) 
		 
	def __unicode__(self):
		return self.titulo
	
	def is_favorite(self, user):
		try:
		    Favoritas.objects.get(oferta=self, usuario = user)
		    return True
		except ObjectDoesNotExist:
			return False
		

class Favoritas(models.Model):
	oferta = models.ForeignKey(Oferta)
	usuario = models.ForeignKey(Profile)
	
	def __unicode__(self):
		return self.oferta.titulo
		