import asyncio
import json
import random

from channels.generic.websocket import AsyncWebsocketConsumer

class RandomNumberConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.task = asyncio.create_task(self.send_random_numbers())

    async def send_random_numbers(self):
        while True:
            number = random.randint(1, 100)
            await self.send(text_data=json.dumps({'number': number}))
            await asyncio.sleep(5)
    
    async def receive(self, text_data):
        text_data = json.loads(text_data)
        message = text_data['massage']
        response = f'Received message: {message}'
        await self.send(text_data=json.dumps({'response': response}))

    async def disconnect(self, close_code):
        self.task.cancel()
        await self.task
        await self.close()