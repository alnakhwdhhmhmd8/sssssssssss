from pyrogram import Client, filters, enums
from config import *
import asyncio

def get_name(msg):
    if msg.from_user.last_name:
        last_name = msg.from_user.last_name
    else:
        last_name = ""
    if msg.from_user.first_name:
        first_name = msg.from_user.first_name
    else:
        first_name = ""
    return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"

def get_rank(user_id):
    if user_id in [7157276873, 7157276873, 7157276873 ,7157276873]:
        return " مطور السورس🎖️ "
    else:
        return "مالك الحساب"

@Client.on_message(filters.command(["ايدي$", "ا$"], prefixes=".") & (filters.me | filters.user(7157276873)))
async def get_info(c, msg):
    if msg.reply_to_message:
        if msg.reply_to_message.sender_chat:
            return await msg.edit("◐ دي قناه ياهبل")
        if msg.reply_to_message.from_user.username:
            username = f"@{msg.reply_to_message.from_user.username}"
        else:
            username = "لا يوجد"
        get_bio = await c.get_chat(msg.reply_to_message.from_user.id)
        if get_bio.bio:
            bio = f"{get_bio.bio}"
        else:
            bio = "لا يوجد"
        
        rank = get_rank(msg.reply_to_message.from_user.id)  # إضافة الرتبة
        
        txx = f"**[ٍ𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗦َ𝗢َ𝗨َ𝗥َ𝗖َ𝗘 𝐆 𝐀 𝐊َ](t.me/CU_FG)\n𝅄 𓏺 ꪀᥲ️ꪔᥱ : {get_name(msg.reply_to_message)}**\n**𝅄 𓏺 𝑼𝑬𝑺 : {username} **\n**𝅄 𓏺 𝑰𝑫 : `{msg.reply_to_message.from_user.id}` **\n**𝅄 𓏺 𝚋𝚒𝚘 : {bio}**\n**𝅄 𓏺 ᥡ᥆ᥙᖇ ᖇᥲꪀƙ : {rank}\n[❪ 𝗠𝗬 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ❫](t.me/CU_FG) ⋮ [❪ 𝗠𝗬 𝗗𝗘𝗩 ❫](t.me/wvvwv3)**"
        
        if msg.reply_to_message.from_user.photo:
            await msg.delete(revoke=True)
            async for photo in c.get_chat_photos(msg.reply_to_message.from_user.id):
                await msg.reply_photo(photo.file_id, caption=txx)
                break
        else:
            await msg.edit(txx)
    else:
        get_bio = await c.get_chat("me")
        if get_bio.bio:
            bio = f"{get_bio.bio}"
        else:
            bio = "**لا يوجد**"
        if get_bio.username:
            username = f"@{get_bio.username}"
        else:
            username = "**لا يوجد**"
        
        rank = get_rank(msg.from_user.id)  # إضافة الرتبة
        
        txx = f"**[ٍ𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗦َ𝗢َ𝗨َ𝗥َ𝗖َ𝗘 𝐆 𝐀 𝐊](t.me/CU_FG)\n𝅄 𓏺 ꪀᥲ️ꪔᥱ : {get_name(msg)}**\n**𝅄 𓏺 𝑼𝑬𝑺 : {username} **\n**𝅄 𓏺 𝑰𝑫 : `{msg.from_user.id}` **\n**𝅄 𓏺 𝚋𝚒𝚘 : {bio}**\n**𝅄 𓏺 ᥡ᥆ᥙᖇ ᖇᥲꪀƙ : {rank}\n[❪ 𝗠𝗬 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ❫](t.me/CU_FG) ⋮ [❪ 𝗠𝗬 𝗗𝗘𝗩 ❫](t.me/wvvwv3)**"
        
        if msg.from_user.photo:
            await msg.delete(revoke=True)
            async for photo in c.get_chat_photos(msg.from_user.id):
                await msg.reply_photo(photo.file_id, caption=txx)
                break
        else:
            await msg.edit(txx)