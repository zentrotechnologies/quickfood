from django.db import models
from menu.models import *
# Create your models here.

class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_ACCEPTED = 'accepted'
    STATUS_PREPARING = 'preparing'
    STATUS_READY = 'ready'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELLED = 'cancelled'

    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_PREPARING, 'Preparing'),
        (STATUS_READY, 'Ready for pickup'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    customer_name = models.CharField(max_length=200, blank=True)  # optional
    customer_phone = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pickup_code = models.CharField(max_length=20, blank=True)  # numeric code for pickup / QR

    def __str__(self):
        return f"Order {self.id} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)  # snapshot of name
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.CharField(max_length=255, blank=True)

    def line_total(self):
        return self.price * self.quantity
