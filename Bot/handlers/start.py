from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from Bot import app

@app.on_message(filters.command("start"))
async def lund(c : Client , m : Message):
    text = "Loda Lele"
    await m.reply_text(text)