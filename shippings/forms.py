from django.forms import ModelForm, TextInput
from shippings.models import Envio

class PrealertForm(ModelForm):
    class Meta:
        model = Envio
        exclude = ['pais','ciudad','proveedor','tipo',]
        

