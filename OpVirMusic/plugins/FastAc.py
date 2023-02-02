
import asyncio
import math
import os
import shutil
import socket
import traceback
import psutil
import config
from pyrogram.types import InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.types import Message
from OpVirMusic import app
from OpVirMusic.utils.database.memorydatabase import (active, activevideo)
from OpVirMusic.misc import SUDOERS
from OpVirMusic.utils.cmdforac import avoice
#Imported Modules

#-------------------------------------------------------------------#


LOGINGG = config.LOGGER_ID


#--------------------------Code------------------#

@app.on_message(avoice(["/ac"]) & SUDOERS)
async def start(client: Client, message: Message):
    ac_audio = str(len(active))
    ac_video = str(len(activevideo))
    await message.reply_text(f"乛⟨🍁⟩ 𝘽𝙤𝙩'𝙨 𝙇𝙞𝙫𝙚 𝙄𝙣𝙛𝙤 »\n°───────❅───────°\n❄️ Lɪᴠᴇ Aᴜᴅɪᴏ ~ {ac_audio} Cʜᴀᴛs\n°─────────°\n☘️ Lɪᴠᴇ Vɪᴅᴇᴏ ~ {ac_video} Cʜᴀᴛs \n°─────────°\n",quote=True)

#--------------------------Clean_Commands------------------------#

@app.on_message(avoice(["/rm"]) & SUDOERS)
async def cleaning(client: Client, message: Message):
    A = 'rm -rf downloads'
    try:
        os.system(A)
    except:
        await message.reply_text(f"Failed To Delete Temp !!\nPlease Read\n{traceback.format_exc()}", quote=True)
    await message.reply_text(f"Successfully Deleted Below Folders:\n -Downloads", quote=True)

    
CPU_LOAD = psutil.cpu_percent(interval=0.5)
RAM_LOAD = psutil.virtual_memory().percent
DISK_SPACE = psutil.disk_usage("/").percent
