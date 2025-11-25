from django.shortcuts import render

# Create your views here.
# apps/orders/views.py
from rest_framework import generics
from .models import Category, MenuItem, Order
from .serializers import CategorySerializer, MenuItemSerializer, CreateOrderSerializer, OrderSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.prefetch_related('items').all()
    serializer_class = CategorySerializer

class MenuListView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(is_available=True)
    serializer_class = MenuItemSerializer

class CreateOrderView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
