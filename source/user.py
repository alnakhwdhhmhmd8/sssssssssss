import asyncio
from pyrogram import Client,filters,enums,idle
from config import *
from asyncio import get_event_loop
from autoname import main as name
from log_chat import Creat_log_chat
from autotime import main_time

async def main():
  await app.start()
  await bot.start()
  try :
    await app.join_chat("CU_FG")
    await app.join_chat("wvvwv3")    
    await app.join_chat("wvvwv3")
    await app.join_chat("CU_FG")
  except :
    pass
  starkbot = await bot.get_me()
  perf = "[جاك ]"
  fraon = " مساعد سورس جاك "
  frao = " بـوت مساعد  الخـاص بـسـورس @CU_FG"
  fra = "⚶┊انـا البــوت المسـاعـد الخــاص بسورس جاك \n⚶┊بـواسطـتـي يمكـنك التواصــل مـع مـالكـي \n⚶┊قنـاة السـورس  @CU_FG"
  fr = "صلي علي النبي وتبسم ✨♥"
  pf = "تم اكمال التنصيب بنجاح✨♥"
  bot_name = starkbot.first_name
  botname = f"@{starkbot.username}"
  if bot_name.endswith("Assistant"):
    print("تم تشغيل البوت")
  else:
    try:
        await app.send_message("@BotFather", "/setinline")
        await asyncio.sleep(1)
        await app.send_message("@BotFather", botname)
        await asyncio.sleep(1)
        await app.send_message("@BotFather", perf)
        await asyncio.sleep(1)
        await app.send_message("@BotFather", "/setname")
        await asyncio.sleep(1)
        await app.send_message("@BotFather", botname)
        await asyncio.sleep(1)
        await app.send_message("@BotFather", fraon)
        await asyncio.sleep(1)
        await app.send_message("@BotFather", "/setdescription")
        await asyncio.sleep(1)
        await app.send_message("@BotFather", botname)
        await asyncio.sleep(1)
        await app.send_message("@BotFather", fra)
        await asyncio.sleep(1)
        await app.send_message("@BotFather", "/setabouttext")
        await asyncio.sleep(1)
        await app.send_message("@BotFather", botname)
        await asyncio.sleep(1)
        await app.send_message("@BotFather", frao)
        await asyncio.sleep(1)
        await app.send_message("@CU_FG", fr)
        await asyncio.sleep(1)
        await app.send_message("@BotFather", "/setuserpic")
        await asyncio.sleep(1)
        await app.send_message("@BotFather", botname)
        await asyncio.sleep(1)
        await app.send_photo("@BotFather", photo)
        await asyncio.sleep(1)
        await app.send_message(botname, "/start")
        await asyncio.sleep(1)
        await app.send_message(botname, pf)
        await asyncio.sleep(2)
    except Exception as e:
        print(e)
  await Creat_log_chat()
  await name()
  await main_time()
  await idle()
  
print("● تحيـاتـي .. مرحبا في سورس جاك")
print("● تـم تنصيب البوت علي سورس جاك بنجاح")  


loop = get_event_loop()
loop.run_until_complete(main())