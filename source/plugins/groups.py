from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
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


async def is_Admin(chat, id):
    admins = []
    async for m in app.get_chat_members(chat, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admins.append(m.user.id)
    if id in admins:
        return True
    else:
        return False

@Client.on_message(filters.command("ضبط", prefixes=f".") & filters.me & ~filters.reply)
async def vars_edit(c, m):
    list_ = m.text.split(' ', 2)
    if len(list_) < 2:
        await m.edit("**الصيغه غلط !!**")
        return
    var = m.text.split(' ', 2)[1]
    if len(list_) == 3:
        input_text = m.text.split(' ', 2)[2]
    else:
        await m.edit("**الصيغه غلط !!**")
        return
    r.set(f"{sudo_id}:{var}", input_text)
    await m.edit( 
    f"**تم ضبط** `{var}` .!!"
    )
    return

@Client.on_message(filters.command("ضبط", prefixes=f".") & filters.me & filters.reply)
async def vars_edit_r(c, m):
    list_ = m.text.split(' ', 1)
    if len(list_) < 1:
        await m.edit("**الصيغه غلط !!**")
        return
    var = m.text.split(' ', 1)[1]
    input_text = m.reply_to_message.text if m.reply_to_message.text else m.reply_to_message.caption
    r.set(f"{sudo_id}:{var}", input_text)
    await m.edit( 
    f"**تم ضبط** `{var}` .!!"
    )
    return

@Client.on_message(filters.command("الغاء ضبط", prefixes=f".") & filters.me)
async def vars_del(c, m):
    list_ = m.text.split(' ', 2)
    if len(list_) < 2:
        await m.edit("**الصيغه غلط !!**")
        return
    var = m.text.split(' ', 2)[2]
    r.delete(f"{sudo_id}:{var}")
    await m.edit( 
    f"**تم مسح** `{var}` .!!"
    )
    return

@Client.on_message(filters.command("مسح المشرفين$", prefixes=f".") & filters.me & filters.group)
async def delADMINISTRATORS(c, m):
    num_d = 0
    num_f = 0
    msg = await m.edit('**جاري مسح المشرفين .!!**')
    async for mem in app.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        try:
            await m.chat.promote_member(
                user_id=mem.user.id,
                privileges=ChatPrivileges(
                    can_manage_chat=False,
                    can_restrict_members=False,
                    can_promote_members=False,
                    can_delete_messages=False,
                    can_manage_video_chats=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False,
                    is_anonymous=False
                )
            )
            num_d += 1
        except Exception as e:
            num_f += 1
        await msg.edit(f'تم تنزيل `{num_d}` مشرف\nفشل في تنزيل `{num_f}` مشرف\n.')
    await msg.edit(f'تم تنزيل `{num_d}` مشرف\nفشل في تنزيل `{num_f}` مشرف\nخلصت ✅')

@Client.on_message(filters.command("رفع مشرف", prefixes=f".") & filters.me & filters.reply & filters.group)
async def Promote_m(c, m):
    list_ = m.text.split(' ', 2)
    state = (await c.get_chat_member(m.chat.id, c.me.id))
    if state.status == enums.ChatMemberStatus.OWNER:
        try:
            await m.chat.promote_member(
                user_id=m.reply_to_message.from_user.id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_restrict_members=False,
                    can_promote_members=False,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_change_info=False,
                    can_invite_users=True,
                    can_pin_messages=True,
                    is_anonymous=False
                )
            )
            if len(list_) == 3:
                Title = m.text.split(' ', 2)[2]
            else:
                Title = "مشرف"
            await c.set_administrator_title(m.chat.id, m.reply_to_message.from_user.id, Title)
            await m.edit(f'**رفعته ( {Title} ) !!**')
        except Exception as e:
            await m.edit(f'**حدث خطأ..**\n\n`{e}`')
            print(e)
        return
    if state.status == enums.ChatMemberStatus.ADMINISTRATOR:
        if not state.privileges.can_promote_members:
            await m.edit('**ممعيش صلاحيات !!**')
            return
        try:
            await m.chat.promote_member(
                m.reply_to_message.from_user.id,
                privileges=ChatPrivileges(
                can_manage_chat=True,
                can_restrict_members=False,
                can_promote_members=False,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                is_anonymous=False
                ),
            )
            if len(list_) == 3:
                Title = m.text.split(' ', 2)[2]
            else:
                Title = "مشرف"
            await c.set_administrator_title(m.chat.id, m.reply_to_message.from_user.id, Title)
            await m.edit(f'**رفعته ( {Title} ) !!**')
        except Exception as e:
            await m.edit(f'**حدث خطأ..**\n\n`{e}`')
            print(e)
        return
    else:
        await m.edit('**انا عضو فقير !!**')
        return


@Client.on_message(filters.command("تنزيل مشرف$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def dePromote_m(c, m):
    state = (await c.get_chat_member(m.chat.id, c.me.id))
    if state.status == enums.ChatMemberStatus.OWNER:
        try:
            await m.chat.promote_member(
                user_id=m.reply_to_message.from_user.id,
                privileges=ChatPrivileges(
                    can_manage_chat=False,
                    can_restrict_members=False,
                    can_promote_members=False,
                    can_delete_messages=False,
                    can_manage_video_chats=False,
                    can_change_info=False,
                    can_invite_users=False,
                    can_pin_messages=False,
                    is_anonymous=False
                )
            )
            await m.edit('**نزلته !!**')
        except Exception as e:
            await m.edit(f'**حدث خطأ..**\n\n`{e}`')
            print(e)
        return
    if state.status == enums.ChatMemberStatus.ADMINISTRATOR:
        if not state.privileges.can_promote_members:
            await m.edit('**ممعيش صلاحيات !!**')
            return
        try:
            await m.chat.promote_member(
                m.reply_to_message.from_user.id,
                privileges=ChatPrivileges(
                can_manage_chat=False,
                can_restrict_members=False,
                can_promote_members=False,
                can_delete_messages=False,
                can_manage_video_chats=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                is_anonymous=False
                ),
            )
            await m.edit('**نزلته !!**')
        except Exception as e:
            await m.edit(f'**حدث خطأ..**\n\n`{e}`')
            print(e)
        return
    else:
        await m.edit('**انا عضو فقير !!**')
        return
      
@Client.on_message(filters.command("قبول الطلبات",".") & filters.me)
async def app_allreq(c,msg): 
   try: 
     await c.approve_all_chat_join_requests(msg.chat.id) 
     await msg.edit("• تم قبول جميع الريكويستات") 
   except: 
     await msg.edit("• عذرا عزيزي لكنك لست ادمن")
     
     
@app.on_message(filters.command("الرابط",".") & filters.me)
async def linnkkkk(client: Client, message: Message):
    tex = await message.edit("جاري انشاء رابط . . .")
    chid = message.chat.id
    link = await client.export_chat_invite_link(chid)
    await tex.edit_text(f"تـم جلب الرابط \n\n• {link}")
     
@Client.on_message(filters.command("اطردني$", prefixes=f".") & filters.me)
async def leave(c,msg):
    await c.leave_chat(msg.chat.id)
    
@Client.on_message(filters.command("حذف صورة$", prefixes=f".") & filters.me)
async def delfoto(c,msg):
    await c.delete_chat_photo(msg.chat.id)
    

@Client.on_message(filters.regex(".ضع اسم (.*?)") & filters.me)
async def set_name(c,msg):
    name = msg.text.replace(".ضع اسم " ,"")
    await c.set_chat_title(msg.chat.id, name)


@Client.on_message(filters.regex(".ضع صوره (.*?)") & filters.me)
async def set_photo(c,msg):
    name = msg.text.replace(".ضع صوره " ,"")
    await c.set_chat_photo(msg.chat.id, name)
 # == == == == == == == == == == == == == == == == == == == ==  
@Client.on_message(filters.command("حفظ$", prefixes=f".") & filters.me)
async def save(c, msg):
    await c.add_contact(msg.chat.id)
 
@Client.on_message(filters.command("كتم$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def mute(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("◐ لا يمكنك استخدام الامر علي مبرمجين السورس")
    chek = await is_Admin(msg.chat.id, msg.from_user.id)
    if chek == False:
        await message.reply("◐ يجب ان تكون مشرف بالمجموعه لاستخدام الاوامر")
        return False
    try:
        if msg.reply_to_message.from_user.id == sudo_id:
            return await msg.edit("مينفعش تكتم نفسك")
        if msg.reply_to_message.from_user.id == 7157276873:
            return await msg.edit("◐ لا يمكنك كتم المطور جاك باشا ")
        if msg.reply_to_message.from_user.id == 7157276873:
            return await msg.edit("لايمكنك كتم المطور جاك")
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.from_user.id)
        txx = f"◐ العضو {get_name(msg.reply_to_message)} \n◐ تم كتمه بنجاح"
        await msg.edit(txx)
    except:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("◐ تم كتم القناه في المجموعه")


@Client.on_message(filters.command("الغاء كتم$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def un_mute(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("◐ لا يمكنك استخدام الامر علي مبرمجين السورس")
    try:
        if msg.reply_to_message.from_user.id == sudo_id:
            return await msg.edit("◐ لا يمكنك  الغاء كتم نفسك")
        if msg.reply_to_message.from_user.id == 7157276873:
            return await msg.edit("◐ لا يمكنك الغاء كتم المطور جاك باشا ")
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.from_user.id)
        txx = f"◐ العضو {get_name(msg.reply_to_message)} \n◐ تم الغاء كتمه بنجاح"
        await msg.edit(txx)
    except:
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("◐ تم الغاء كتم القناه في المجموعه")


@Client.on_message(filters.command("مسح المكتومين", prefixes=f".") & filters.me & filters.group)
async def un_mute_all(c, msg):
    r.delete(f"{sudo_id}mute{msg.chat.id}")
    txx = f"◐ تم مسح المكتومين بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("حظر$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def bann(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("◐ لا يمكنك استخدام الامر علي مبرمجين السورس")
    chek = await is_Admin(msg.chat.id, msg.from_user.id)
    if chek == False:
        await message.reply("◐ يجب ان تكون مشرف بالمجموعه لاستخدام الاوامر")
        return False
    if msg.reply_to_message.sender_chat:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("◐ تم كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("◐ لا يمكنك حظر نفسك")
    if msg.reply_to_message.from_user.id == 7157276873:
        return await msg.edit("◐ لا يمكنك حظر المطور جاك باشا ")
    try:
        await c.ban_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
        txx = f"◐ العضو {get_name(msg.reply_to_message)} \n◐ تم حظره بنجاح"
        await msg.edit(txx)
    except Exception as e:
        await msg.edit(f"◐ ليس لديك صلاحيات الحظر في المجموعه")


@Client.on_message(filters.command("الغاء حظر$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def un_ban(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("◐ لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("◐ تم الغاء كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("◐ لا يمكنك  الغاء حظر نفسك")
    if msg.reply_to_message.from_user.id == 7157276873:
        return await msg.edit("◐ لا يمكنك الغاء حظر المطور جاك باشا ")
    try:
        await c.unban_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
        txx = f"◐ العضو {get_name(msg.reply_to_message)} \n◐ تم الغاء حظره بنجاح"
        await msg.edit(txx)
    except:
        await msg.edit("◐ العضو ليس محظور \n◐ او ليس لديك صلاحيات الحظر في المجموعه")


@Client.on_message(filters.command(["مسح المحظورين$", "مسح المطرودين$"], prefixes=f".") & filters.me & ~filters.private)
async def un_ban_all(c, msg):
    xxx = 0
    async for m in c.get_chat_members(msg.chat.id, filter=enums.ChatMembersFilter.BANNED):
        try:
            await c.unban_chat_member(msg.chat.id, m.user.id)
            xxx += 1
        except:
            pass
    await msg.edit(f"◐ تم الغاء حظر {xxx} عضو")


@Client.on_message(filters.command("تدمير$", prefixes=f".") & filters.me & ~filters.private)
async def ban_all_members(c, msg):
    xxx = 0
    un = 0
    async for m in c.get_chat_members(msg.chat.id):
        try:
            if m.user.id == sudo_id:
                continue
            await c.ban_chat_member(msg.chat.id, m.user.id)
            if xxx % 10 == 0:
                await msg.edit(f"◐ تم حظر {xxx}")
            xxx += 1
        except:
            un += 1
    await msg.edit(f"◐ تم حظر {xxx} عضو\n◐ لم استطيع حظر {un} عضو")


@Client.on_message(filters.command("كتم عام$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def mute_all(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("◐ لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("◐ تم كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("◐ لا يمكنك كتم نفسك")
    if msg.reply_to_message.from_user.id == 7157276873:
        return await msg.edit("◐ لا يمكنك كتم المطور جاك باشا ")
    if msg.reply_to_message.from_user.id == 7157276873:
        return await msg.edit("لا يمكنك كتم المطور جاك")
    r.sadd(f"{sudo_id}mute", msg.reply_to_message.from_user.id)
    txx = f"◐ العضو {get_name(msg.reply_to_message)} \n◐ تم كتمه عام بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command(
    ["الغاء كتم عام$", "الغاء كتم العام$", "الغاء الكتم العام$", "الغاء العام$", "الغاء الحظر العام$", "الغاء حظر عام$",
     "الغاء حظر العام$"], prefixes=f".") & filters.me & filters.reply & filters.group)
async def un_mute_all_user(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("◐ لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.srem(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("◐ تم الغاء كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("◐ لا يمكنك  الغاء كتم نفسك")
    if msg.reply_to_message.from_user.id == 7157276873:
        return await msg.edit("◐ لا يمكنك الغاء كتم المطور جاك باشا ")
    r.srem(f"{sudo_id}mute", msg.reply_to_message.from_user.id)
    r.srem(f"{sudo_id}ban", msg.reply_to_message.from_user.id)
    txx = f"◐ العضو {get_name(msg.reply_to_message)} \n◐ تم الغاء كتمه/حظره عام بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("مسح قائمه العام$", prefixes=f".") & filters.me & filters.group)
async def un_mute_all_3am(c, msg):
    r.delete(f"{sudo_id}mute")
    r.delete(f"{sudo_id}ban")
    txx = f"◐ تم مسح المكتومين/المحظورين عام بنجاح"
    await msg.edit(txx)


@Client.on_message(filters.command("حظر عام$", prefixes=f".") & filters.me & filters.reply & filters.group)
async def ban_all(c, msg):
    if msg.reply_to_message.from_user.id in sudo_command:
        return await msg.edit("◐ لا يمكنك استخدام الامر علي مبرمجين السورس")
    if msg.reply_to_message.sender_chat:
        r.sadd(f"{sudo_id}mute{msg.chat.id}", msg.reply_to_message.sender_chat.id)
        await msg.edit("◐ تم كتم القناه في المجموعه")
        return
    if msg.reply_to_message.from_user.id == sudo_id:
        return await msg.edit("◐ لا يمكنك حظر نفس+  ك")
    if msg.reply_to_message.from_user.id == 7157276873:
        return await msg.edit("◐ لا يمكنك حظر المطور جاك باشا ")
    if msg.reply_to_message.from_user.id == 7157276873:
        return await msg.edit("لايمكنك حظر المطور جاك")
    r.sadd(f"{sudo_id}ban", msg.reply_to_message.from_user.id)
    txx = f"◐ العضو {get_name(msg.reply_to_message)} \n◐ تم حظره عام بنجاح"
    await msg.edit(txx)
