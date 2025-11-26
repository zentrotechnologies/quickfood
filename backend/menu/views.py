from django.shortcuts import render

# Create your views here.
# apps/orders/views.py
from rest_framework import generics
from .models import *
from .serializers import *

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.prefetch_related('items').all()
    serializer_class = CategorySerializer

class MenuListView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(is_available=True)
    serializer_class = MenuItemSerializer