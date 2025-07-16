import asyncio

from pyrogram.client import Client
from config import api_id, api_hash

async def main():
    async with Client("tg_analytics", api_id=api_id, api_hash=api_hash) as app:
        async for message in app.get_chat_history("BDataScienceM", limit=7, offset=0):
            if message.text:
                print(message.text)
            elif message.caption:
                print(message.caption)
            elif message.media:
                print(message.media)
            
            async for reply in app.get_discussion_replies(chat_id="BDataScienceM", message_id=message.id):
                print(f"Reply: {reply.text}")
            print("--------------------------------")

asyncio.run(main())
