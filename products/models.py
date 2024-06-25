# api/models.py
from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    stock = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.name

