import asyncio
from AtiyaMusic import app
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message

@app.on_message(filters.command(["sudolist"]) & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_text(
        text=f"💔 <b>ᴏᴡɴᴇʀs:</b>\n1➤ <a href='https://t.me/iTZViR99'>𓆩🍁𓆪【𓆩𝐑𝐎𝐂𝐊𝐒𓆪】 ͢ ̶̶ͥ ̶ ̶ͣ ͓ ̶͓ͫ➳🇻ιɾ⛦⃕͜🇮🇳</a>",
        disable_web_page_preview=True,
        parse_mode="html"
    )
