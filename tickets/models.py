from django.db import models
from django.utils.translation import ugettext_lazy as _
from profiles.models import Profile

class Ticket(models.Model):
	nombre = models.CharField(_("Nombre"), blank=False, max_length=255)
	email = models.EmailField(_("Email"), blank=False )
	telefono = models.CharField(_("Telefono"), blank=True, max_length=255) 
	mensaje = models.TextField(_("Mensaje"), blank=False)
	SUBJECTS_CHOICES = (
        ('1', 'Queja o reclamo'),
        ('2', 'Sugerencia'),
        ('3', 'Mi paquete no llego'),
        ('4', 'He recibido un paquete que no fue solicitado'),
        ('5', 'Necesito asesoria para utilizar Cittybox'),
    )
	subject = models.CharField(_("Tema"), max_length=1, choices=SUBJECTS_CHOICES)
	usuario = models.ForeignKey(Profile, blank=True, null=True)

	def __unicode__(self):
		return "%s - por %s" % (Ticket.SUBJECTS_CHOICES[int(self.subject)-1][1], self.usuario)