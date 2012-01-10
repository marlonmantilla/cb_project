from django.forms import ModelForm
from offers.models import Producto

class ProductForm(ModelForm):
    class Meta:
        model = Producto
        exclude = ['usuario']
        