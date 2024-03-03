from tqdm import tqdm
import asyncio
import websockets
import time

async def request_for_txt23d(text):
    uri = "ws://0.0.0.0:8765"
    async with websockets.connect(uri) as websocket:
        
        await websocket.send(text)
        print(f'Client sent: {text}')
        greeting = await websocket.recv()
        print(f"Client received: {greeting}")

        return greeting