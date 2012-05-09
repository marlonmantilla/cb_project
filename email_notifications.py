from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import get_template
from django.template import Context
from settings import MEDIA_URL

CITTYBOX_ADMINS = ['marlon.mantilla@hotmail.com']

def send_status_notification(envio):
	htmly = get_template('emails/status_change.html')
	d = Context({ 'user': envio.usuario.user, 'MEDIA_URL': MEDIA_URL, 'envio': envio })
	html_content = htmly.render(d)
	subject, from_email, to = 'Notificacion de paquete', 'no-reply@cittybox.com', envio.usuario.user.email
	send_email_notification(subject, html_content, from_email, [to])
	
def send_prealert_notification(request, envio):
	htmly = get_template('emails/prealert_notification.html')
	d = Context({ 'user': request.user, 'MEDIA_URL': MEDIA_URL, 'envio': envio })
	html_content = htmly.render(d)
	subject, from_email, to = 'Paquete prealertado en Cittybox', 'no-reply@cittybox.com', request.user.email
	send_email_notification(subject, html_content, from_email, [to])
	send_prealert_notification_to_admins(request, envio)

def send_email_notification(subject, html_content, from_email, to):
	msg = EmailMessage(subject, html_content, from_email, to )
	msg.content_subtype = "html"
	msg.send()

def send_prealert_notification_to_admins(request, envio):
	htmly = get_template('emails/admin_prealert_notification.html')
	d = Context({ 'user': request.user, 'MEDIA_URL': MEDIA_URL, 'envio': envio })
	html_content = htmly.render(d)
	subject, from_email = '%s a prealertado en Cittybox' % request.user.first_name, 'no-reply@cittybox.com'
	send_email_notification(subject, html_content, from_email, CITTYBOX_ADMINS )