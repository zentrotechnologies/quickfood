# apps/orders/serializers.py
from rest_framework import serializers
from .models import *



class OrderItemCreateSerializer(serializers.Serializer):
    menu_item_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)
    notes = serializers.CharField(allow_blank=True, required=False)

class CreateOrderSerializer(serializers.Serializer):
    customer_name = serializers.CharField(allow_blank=True, required=False)
    customer_phone = serializers.CharField(allow_blank=True, required=False)
    notes = serializers.CharField(allow_blank=True, required=False)
    items = OrderItemCreateSerializer(many=True)

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Order must have at least one item.")
        return value

    def create(self, validated_data):
        from .models import Order, OrderItem, MenuItem
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total = 0
        for it in items:
            menu = MenuItem.objects.get(id=it['menu_item_id'])
            oi = OrderItem.objects.create(
                order=order,
                menu_item=menu,
                name=menu.name,
                price=menu.price,
                quantity=it['quantity'],
                notes=it.get('notes','')
            )
            total += oi.price * oi.quantity
        order.total_amount = total
        # generate pickup code (e.g., last 6 digits of UUID or random numeric)
        order.pickup_code = str(abs(hash(order.id)) % 1000000).zfill(6)
        order.save()
        return order

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id','created_at','status','customer_name','customer_phone','notes','total_amount','pickup_code','items']

    def get_items(self, obj):
        return [{
            'name': i.name,
            'price': i.price,
            'quantity': i.quantity,
            'notes': i.notes
        } for i in obj.items.all()]
