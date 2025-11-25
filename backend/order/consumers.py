# apps/orders/consumers.py
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class OrderConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # expect order_id passed as query param: ?order_id=<uuid>
        self.order_id = self.scope['url_route']['kwargs'].get('order_id')
        if not self.order_id:
            await self.close()
            return
        self.group_name = f"order_{self.order_id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def order_status(self, event):
        # event contains {'type':'order_status', 'data': {...}}
        await self.send_json(event['data'])
