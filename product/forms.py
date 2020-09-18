from django import forms
from django.forms import modelformset_factory

from .models import ModelProduct, ModelUser


class NameForm(forms.Form):
    name = forms.CharField(max_length=20)
    status = forms.CharField(max_length=20)
    user = forms.ModelChoiceField(queryset=ModelUser.objects.all())
    file = forms.FileField()


class ProductForm(forms.ModelForm):
    class Meta:
        model = ModelProduct
        fields = ('name', 'code', 'product', 'user')


ProductFormSet = modelformset_factory(ModelProduct, fields=('code', 'product'), extra=1, )
