from django.db import models


class ModelItem(models.Model):
    item = models.CharField(max_length=20)
    state = models.CharField(max_length=10)

    def __str__(self):
        return self.item


class ModelProduct(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    product = models.CharField(max_length=30)

    def __str__(self):
        return self.name


