from django import forms
from .models import ModelProduct


class FormProduct(forms.ModelForm):
    class Meta:
        model = ModelProduct
        fields = ('name', 'code', 'product')
