from django import forms
from django.forms import modelformset_factory

from .models import ModelProduct


class NameForm(forms.Form):
    name = forms.CharField(max_length=20)


class ProductForm(forms.ModelForm):
    class Meta:
        model = ModelProduct
        fields = ('name', 'code', 'product')


ProductFormSet = modelformset_factory(ModelProduct, fields=('code', 'product'), extra=5,)
