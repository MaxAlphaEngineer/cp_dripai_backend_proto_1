import json
import socket
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class TicTacToeConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        print("Connecting")
        await self.accept()


