from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import ModelProduct
from .forms import ProductForm, ProductFormSet, NameForm


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
    form_class = ProductForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super(CreateProduct, self).get_context_data(**kwargs)
        context['formset'] = ProductFormSet(queryset=ModelProduct.objects.none())
        context['name_form'] = NameForm()
        return context

    def post(self, request, *args, **kwargs):
        formset = ProductFormSet(request.POST)
        name_form = NameForm(data=request.POST, files=request.FILES)
        if formset.is_valid() and name_form.is_valid():
            return self.form_valid(formset, name_form)

    def form_valid(self, formset, name_form):
        name = name_form.cleaned_data['name']
        status = name_form.cleaned_data['status']
        user = name_form.cleaned_data['user']
        file = name_form.cleaned_data['file']
        instances = formset.save(commit=False)
        for instance in instances:
            instance.name = name
            instance.status = status
            instance.user = user
            instance.file = file
            instance.save()
        return HttpResponseRedirect('/')
