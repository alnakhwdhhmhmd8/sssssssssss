from pyrogram import Client, filters, enums
from config import *
import os, time

os.environ['TZ'] = 'Africa/Cairo'
time.tzset()


@Client.on_message(filters.private & ~filters.bot)
async def pv_cmd(c, msg):
    log_chat = r.get(f"{sudo_id}:LOG_CHAT")
    if msg.from_user.id != sudo_id:
        try:
            await msg.forward(log_chat)
        except:
            if msg.media == enums.MessageMediaType.VIDEO:
                await msg.download("./Ttl.mp4")
                await app.send_video(log_chat, "Ttl.mp4")
                os.remove("./Ttl.mp4")
            elif msg.media == enums.MessageMediaType.PHOTO:
                await msg.download("./Ttl.jpg")
                await app.send_photo(log_chat, "Ttl.jpg")
                os.remove("./Ttl.jpg")
            pass
        if r.sismember(f"{sudo_id}mute_pv", msg.chat.id):
            await msg.delete(revoke=True)
            return
        if r.get(f"{sudo_id}welcome"):
            if not r.sismember(f"{sudo_id}accept", msg.chat.id):
                if r.get(f"{sudo_id}waiting{msg.chat.id}"):
                    r.delete(f"{sudo_id}waiting{msg.chat.id}")
                    await msg.reply("تم ارسال رسالتك بنجاح \n قام النظام بكتمك انتظر حتا يقوم مالك الحساب بالرد عليك")
                    r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
                    r.delete(f"{sudo_id}waiting{msg.chat.id}")
                    return
                r.set(f"{sudo_id}waiting{msg.chat.id}", "on")
                PM_logo = r.get(f"{sudo_id}:PMG_MEDIA") or "https://t.me/CU_FG/1374"
                CHANNEL = r.get(f"{sudo_id}:CHANNEL") or "CU_FG"
                CHANNEL = CHANNEL.replace('@', '')
                PM_text = r.get(f"{sudo_id}:PM_TEXT_CUSTOM") or """**اهلا بيك في شات  المتواضع**
**———————سورس جاك———————**
**Hello my friend  ALMARHEB now convoy**
**———————سورس—————————**
**اولا صلي على النبي ❤️💕(عليه افضل الصلاة والسلام)**
**———————جاك————————**
**صلي علي النبي وتبسم♡**
**You enlightened my private chat, my friend. Leave your message and wait for a response** 

**———————**
**سيب رسالتك هنا  اول ما افتح هرد عليك**

**×——————————**
**🔮انــا 🙋‍♂️نصـحـتك 💁‍♂️ونـت 🫵بـراحـتـك🤷‍♂️**"""
                send = c.send_video if PM_logo.endswith(".mp4") else c.send_photo
                try:
                    await send(
                        msg.chat.id,
                        PM_logo,
                        caption=f"<b>{PM_text}</b>\n\n [◜ 𝗦َ𝗢َ𝗨َ𝗥َ𝗖َ𝗘 𝐆 𝐀 𝐊◞](https://t.me/CU_FG) | [√𝗠𝗬 𝗗𝗘𝗩](https://t.me/wvvwv3) "
                    )
                except Exception as e:
                    print(e)
                    await msg.reply(f"<b>{PM_text}</b>\n\n [◜ 𝗦َ𝗢َ𝗨َ𝗥َ𝗖َ𝗘 𝐆 𝐀 𝐊◞](https://t.me/CU_FG) | [√𝗠𝗬 𝗗𝗘𝗩](https://t.me/wvvwv3)")
                return
    else:
        if msg.text == ".قبول" or msg.text == ".الغاء كتم" or msg.text == ".س":
            r.srem(f"{sudo_id}mute_pv", msg.chat.id)
            r.sadd(f"{sudo_id}accept", msg.chat.id)
            await msg.edit("**◐ تم السماح له بالتحدث 🔔✓**")
        if msg.text == ".رفض" or msg.text == ".ر": 
            r.srem(f"{sudo_id}accept", msg.chat.id)
            await msg.edit("**◐ تم رفض العضو بنجاح 🔇✓**")
        if msg.text == ".كتم" or msg.text == ".ك":
            if msg.chat.id == sudo_id:
                return await msg.edit("**◐ مينفعش تكتم نفسك 😹**")
            if msg.chat.id == 7157276873:
                return await msg.edit("**◐ لا يمكنك كتم المبرمج جاك باشا ❌**")
            if msg.chat.id == 7157276873:
                return await msg.edit("**◐ لا يمكنك كتم المبرمج جاك باشا ❌**")
            r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
            await msg.edit("**◐ تم كتم العضو بنجاح 🔕✓**")


@Client.on_message(filters.group)
async def gp(client, msg):
    log_chat = r.get(f"{sudo_id}:LOG_CHAT")
    current_time = time.strftime('%H:%M')
    chatt = str(msg.chat.id)
    chat = chatt.replace("-100", "").replace("-", "")
    msg_link = f"[ اضغط هنا لعرض الرساله](https://t.me/c/{chat}/{msg.id})"
    if msg.mentioned:
        if msg.from_user:
            try:
                txt = f"◐ لديك منشن من العضو [{msg.from_user.first_name}](tg://user?id={msg.from_user.id}) \n◐ اسم الجروب {msg.chat.title} \n◐ الوقت {current_time} \n{msg_link}"
                await app.send_message(log_chat, txt)
                await msg.forward(log_chat)
            except:
                pass
        else:
            txt = f"◐ لديك منشن من القناه {msg.sender_chat.title} \n◐ اسم الجروب {msg.chat.title} \n◐ الوقت {current_time} \n{msg_link}"
            await app.send_message(log_chat, txt)
            await msg.forward(log_chat)
    if msg.from_user:
        sender_id = msg.from_user.id
    elif msg.sender_chat:
        sender_id = msg.sender_chat.id
    if r.sismember(f"{sudo_id}mute", sender_id) or r.sismember(f"{sudo_id}mute{msg.chat.id}", sender_id):
        try:
            await msg.delete()
        except:
            pass
    if r.sismember(f"{sudo_id}ban", sender_id):
        try:
            await msg.delete()
            await client.ban_chat_member(msg.chat.id, msg.from_user.id)
        except:
            pass
