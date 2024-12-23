from pyrogram import Client, filters
from pyrogram.types import Message
import time
from Bot.config import OWNER_ID  # Import OWNER_ID from config.py
from Bot import StartTime, app  # Importing StartTime and app

# Calculate bot uptime
def get_uptime():
    current_time = time.time()
    uptime = current_time - StartTime
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

@app.on_message(filters.command("alive") & filters.private)
async def alive_command(client: Client, message: Message):
    # Fetch the owner's full Telegram name
    owner = await client.get_users(OWNER_ID)

    # Prepare the alive message
    alive_text = f"""
✨I'm Alive Baby
🥀I'm Working Perfectly
     ▱▱▱▱▱▱▱▱▱▱▱▱
🔱My Owner: [{owner.first_name} {owner.last_name or ''}](https://t.me/{owner.username})
🐍Library Version: Pyrogram v{client.__version__}
🤖Bot Version: v1.0
⚡️My Uptime: {get_uptime()}
     ▱▱▱▱▱▱▱▱▱▱▱▱
"""
    # Send the alive message
    await message.reply_text(alive_text, disable_web_page_preview=True)
