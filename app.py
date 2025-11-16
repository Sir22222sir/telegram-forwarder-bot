
from pyrogram import Client, filters
import os
import asyncio

bot_token = os.environ.get("8580548906:AAGzybEKVaL_uPaIvtDBpcsLcrm438nh1Os")
app = Client("my_bot", bot_token=bot_token)

source_channels = ["@kamyarampus", "@sepahcybery"]
target_channel = "@kamiarano"



@app.on_message(filters.channel & filters.chat(source_channels))
async def forward_message(client, message):
    try:
        await asyncio.sleep(2)
        await message.copy(target_channel)

app.run()
        
    
