from pyrogram import Client, filters

api_id = 32471919
api_hash = "59aa5bf8cfed2b5519313d122e25940b"
app = Client("my_account", api_id=api_id, api_hash=api_hash)

source_channels = ["@kamyarampus", "@sepahcybery"]
target_channel = "@kamiarano"

@app.on_message(filters.channel & filters.chat(source_channels))
async def forward_to_target(client, message):
    await message.copy(chat_id=target_channel)

app.run()
