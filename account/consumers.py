from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NoticeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.user_name = self.scope['url_route']['kwargs']['user_name']
        await self.channel_layer.group_add(self.user_name, self.channel_name)

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(self.user_name, self.channel_name)
        
    async def user_event(self, event):
        await self.send(text_data=json.dumps(event,ensure_ascii=False))
