from django.db import models


class ModelProduct(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    product = models.CharField(max_length=30)

    def __str__(self):
        return self.name


