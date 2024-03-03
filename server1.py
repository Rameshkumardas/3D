import asyncio
import datetime
import json
import random
import time
import websockets
from tqdm import tqdm

async def SendMessage(websocket, text, start_time):
    for i in tqdm(range(100)):
        context = {
            "message":text,
            "timeLeft":time.time()-start_time,
            "percentage":i,
        }
        try:
            await websocket.send(json.dumps(context))
        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected.  Do cleanup and Restart")
            break  

        await asyncio.sleep(random.random() * 3)

async def handler(websocket, path):
    text = await websocket.recv()
    start_time = time.time()

    await SendMessage(websocket, text, start_time)

start_server = websockets.serve(handler, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
