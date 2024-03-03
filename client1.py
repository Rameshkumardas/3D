import asyncio
import websockets

async def hello():
    uri = "ws://0.0.0.0:8765"
    count = 5
    async with websockets.connect(uri) as websocket:
        while count > 0:
            greeting = await websocket.recv()
            print(f"< {greeting}")
            count = count - 1

asyncio.get_event_loop().run_until_complete(hello())