# apps/orders/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .serializers import OrderSerializer

@receiver(post_save, sender=Order)
def broadcast_order_status(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    data = OrderSerializer(instance).data
    group = f"order_{instance.id}"
    async_to_sync(channel_layer.group_send)(
        group,
        {
            "type": "order_status",
            "data": {"event": "status_update", "order": data}
        }
    )
