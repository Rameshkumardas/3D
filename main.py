#!/usr/bin/env python

import asyncio
import json
from websockets.server import serve

async def server(websocket):
    text = await websocket.recv()
    context = {
            "message":text,
            "timeLeft":100,
            "percentage":20,
        }
    await websocket.send(json.dumps(context))
    


async def main():
    async with serve(server, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())