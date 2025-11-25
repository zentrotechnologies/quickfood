# apps/orders/models.py
from django.db import models
import uuid

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu/', null=True, blank=True)

    def __str__(self):
        return self.name
