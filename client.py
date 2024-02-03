import asyncio
from websockets.sync.client import connect
import websockets


async def hello():
    # ws_url = "ws://localhost:8765"
    # ws_url = "wss://d38a-41-40-87-34.ngrok-free.app/"
    ws_url = "wss://2f48-41-234-198-139.ngrok-free.app/myHandler"

    async with websockets.connect(ws_url) as websocket:
        await websocket.send("A7la Messa2")
        message = await websocket.recv()
        print(f"Received on client2: {message}")

asyncio.run(hello())

