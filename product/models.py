from django.db import models


class ModelUser(models.Model):
    nickname = models.CharField(max_length=40)
    user_name = models.CharField(max_length=40)

    def __str__(self):
        return self.nickname


class ModelProduct(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    user = models.ForeignKey(ModelUser, on_delete=models.CASCADE)
    product = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.name
