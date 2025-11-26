from django.shortcuts import render

# Create your views here.
# apps/orders/views.py
from rest_framework import generics
from .models import *
from .serializers import *



class CreateOrderView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
