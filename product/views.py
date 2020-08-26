from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import ModelProduct
from .forms import FormProduct


class ListProduct(ListView):
    template_name = 'listProduct.html'
    model = ModelProduct

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = ModelProduct.objects.all()
        return context


class CreateProduct(CreateView):
    template_name = 'createProduct.html'
    model = ModelProduct
    form_class = FormProduct
    success_url = reverse_lazy('main')
