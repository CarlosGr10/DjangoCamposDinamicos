from django.contrib import admin
from .models import ModelProduct, ModelUser
# Register your models here.

admin.site.register(ModelProduct)
admin.site.register(ModelUser)