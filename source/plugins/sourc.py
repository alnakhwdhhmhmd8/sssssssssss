import pyrogram, sys
from pyrogram import Client, filters, enums
from config import *
import asyncio
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton)

pyro = pyrogram.__version__
py = sys.version

@app.on_message(filters.command(["سورس","السورس"], prefixes=f".") & filters.me)
async def ping(app, msg):
  await msg.delete()
  txt = f"""
• 𝗛𝗲𝗹𝗹𝗼 𝗗𝗲𝗮𝗿 : {msg.from_user.mention}
— — — — — — — — —
• 𝗗𝗲𝘃 𝗦𝗼𝘂𝗿𝗰𝗲 : @wvvwv3
• 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗦𝗼𝘂𝗿𝗰𝗲 : @CU_FG
• [𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 {pyro}](https://docs.pyrogram.org/)
• 𝗣𝘆𝘁𝗵𝗼𝗻 {py}
  """
  await app.send_video(msg.chat.id,
  video="https://t.me/WMWBKL/4",
  caption=txt, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="𝐆 𝐀 𝐊 - جاك", url=f"https://t.me/wvvwv3")]]))