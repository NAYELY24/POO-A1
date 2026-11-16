from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        # fields = [
        #     'codigo',
        #     'nombre',
        #     'descripcion',
        #     'precio',
        #     'stock'
        # ]
        fields = '__all__'
