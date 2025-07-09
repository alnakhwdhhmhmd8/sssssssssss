from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio


@bot.on_inline_query(filters.regex("^الابراج$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
               [[
             InlineKeyboardButton("الجدي", callback_data="elgadee"),
             InlineKeyboardButton("الدلو", callback_data="eldaloo"),
             ],
             [
             InlineKeyboardButton("الحوت", callback_data="elhout"),
             InlineKeyboardButton("الحمل", callback_data="elhamal"),
             ],
             [
             InlineKeyboardButton("الثور", callback_data="elthawr"),
             InlineKeyboardButton("الجوزاء", callback_data="elgawzaa"),
             ],
             [
             InlineKeyboardButton("السرطان", callback_data="elsaratan"),
             InlineKeyboardButton("الأسد", callback_data="elaasad"),
             ],
             [
             InlineKeyboardButton("العذراء", callback_data="elazraaa"),
             InlineKeyboardButton("الميزان", callback_data="elmezaan"),
             ],
             [
             InlineKeyboardButton("العقرب", callback_data="elaqrab"),
             InlineKeyboardButton("القوس", callback_data="elqoos"),
             ],
             [
            InlineKeyboardButton("𝗦َ𝗢َ𝗨َ𝗥َ𝗖َ𝗘 َِ𝐆 𝐀 𝐊",url="https://t.me/CU_FG"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="الابراج",
                input_message_content=InputTextMessageContent(
                    "⌔ اهلا بيك بقائمه الابراج اختر ما تريد\n√"
                ),
                url="https://t.me/CU_FG",
                description="𝗦َ𝗢َ𝗨َ𝗥َ𝗖َ𝗘 َِ𝐆 𝐀 𝐊",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )   