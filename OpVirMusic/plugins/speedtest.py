import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from OpVirMusic import app
from OpVirMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⛓️ Rᴜɴɴɪɴɢ Dᴏᴡɴʟᴏᴀᴅ Sᴩᴇᴇᴅᴛᴇsᴛ...**")
        test.download()
        m = m.edit("**🖇️ Rᴜɴɴɪɴɢ Uᴩʟᴏᴀᴅ Sᴩᴇᴇᴅᴛᴇsᴛ...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**🍂 Sʜᴀʀɪɴɢ Sᴩᴇᴇᴅᴛᴇsᴛ Rᴇsᴜʟᴛs...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("☘️ Tʀʏɪɴɢ ᴛᴏ ᴄʜᴇᴄᴋ ᴜᴩʟᴏᴀᴅ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅ...")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""🖇️ **Sᴩᴇᴇᴅᴛᴇsᴛ Rᴇsᴜʟᴛs** 🖇️
    
<u>☛ **Cʟɪᴇɴᴛ ~**</u>
**• __Isᴩ :__** {result['client']['isp']}
**• __Cᴏᴜɴᴛʀʏ :__** {result['client']['country']}
  
<u>☛ **Sᴇʀᴠᴇʀ ~**</u>
**• __Nᴀᴍᴇ :__** {result['server']['name']}
**• __Cᴏᴜɴᴛʀʏ :__** {result['server']['country']}, {result['server']['cc']}
**• __Sᴩᴏɴsᴏʀ :__** {result['server']['sponsor']}
**• __Lᴀᴛᴇɴᴄʏ :__** {result['server']['latency']}  
**• __Pɪɴɢ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
