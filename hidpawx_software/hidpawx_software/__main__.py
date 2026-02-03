import asyncio
from websockets.asyncio.client import connect

from .mm_client import MMAccessClient

async def ping_pawb():
    client = MMAccessClient()
    client.run_forever()

asyncio.run(ping_pawb())