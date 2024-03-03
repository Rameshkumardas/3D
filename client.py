#!/usr/bin/env python

import asyncio
import json
from websockets.sync.client import connect

def Client_Start():

    with connect("ws://0.0.0.0:8765") as websocket:
        websocket.send("Message Description")
        message = websocket.recv()
        print(f"Received From Backend Server: {message}")
        return message
    

Client_Start()