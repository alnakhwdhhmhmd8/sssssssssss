from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
from os import remove
import subprocess
import asyncio
def add_text_to_video(input_file, output_file,text,selected_color,selected_pos,selected_size):
    if "top" in selected_pos:
        y_arg = "10"
    elif "middle" in selected_pos:
        y_arg = "h/2-text_h/2"
    elif "bottom" in selected_pos:
        y_arg = "h-th-10"

    if "left" in selected_pos:
        x_arg = "10"
    elif "center" in selected_pos:
        x_arg = "(w-text_w)/2"
    elif "right" in selected_pos:
        x_arg = "w-text_w-10"
    
    cmd = f"ffmpeg -y -i {input_file} -vf \"drawtext=text='{text}':fontcolor={selected_color}:fontsize={selected_size}:x={x_arg}:y={y_arg}\" -codec:a copy {output_file}"

    try:
        subprocess.check_call(cmd, shell=True)
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}:\n{e.output}")
        return False

reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("عوده",callback_data="help"),
             ]]
             )
txx1 = """
 اهلا بك عزيزي في اوامر الخاص ⇊

⌔︙❬ .تلجراف ❭ بالرد علي الصوره

⌔︙❬ .وش يقول ❭ بالرد علي الصوت 

⌔︙❬ .تغيير اسمي + كتابه الاسم ❭ . تغيير اسمي سوريا

⌔︙❬ .تفعيل الترحيب ❭ 

⌔︙❬ .تعطيل الساعه ❭ 

⌔︙❬ .تفعيل الساعه ❭ 

⌔︙❬ .تعطيل الساعه ❭ 

⌔︙❬ .سبام + كتابه الكلمه + كتابه الرقم ❭ 

⌔︙❬ .سورس ❭ 

⌔︙❬ .قبول ❭ 

⌔︙❬ .رفض ❭ 

⌔︙❬ .كتم ❭ 

⌔︙❬ .الغاء كتم ❭ 

 اوامر الفارت ⇊

⌔︙❬ .ايدي ❭ بالرد علي الشخص

⌔︙❬ `.ضبط PMG_MEDIA ` ❭ لوضع صوره ترحيب في الخاص

⌔︙❬` .الغاء ضبط PMG_MEDIA `❭ للرجوع لصورة الترحيب الافتراضيه

⌔︙❬` .ضبط PM_TEXT_CUSTOM `❭ لتغير النص تحت صورة الترحيب

⌔︙❬ `.الغاء ضبط PM_TEXT_CUSTOM` ❭ لحذف النص والرجوع للنص الافتراضي

⌔︙❬ `.ضبط CHANNEL` ❭ لوضع قناتك في كليشة الترحيب

⌔︙❬ `.الغاء ضبط CHANNEL` ❭ لوضع قناتك في كليشة الترحيب

"""
txx2 = """
 اهلا بك عزيزي في اوامر القنوات والمجموعات ⇊

⌔︙❬ .حظر ❭ ، ❬ .الغاء حظر ❭ 

⌔︙❬ .حظر عام ❭ ، ❬ .الغاء حظر عام ❭ 

⌔︙❬ .مسح المحظورين ❭ ، ❬ .مسح المحظورين عام ❭

⌔︙❬ .كتم ❭ ، ❬ .الغاء كتم ❭ 

⌔︙❬ .كتم عام ❭ ، ❬ .الغاء كتم ❭ 

⌔︙❬ .مسح المكتومين ❭ ، ❬ .مسح المكتومين عام ❭ 

⌔︙❬ .رفع مشرف ❭ + القب [ رفع مشرف سوريا ] 

⌔︙❬ .تنزيل مشرف ❭ ، ❬ .مسح المشرفين ❭ 

⌔︙❬ .مسح رسايله ❭ بالرد علي الشخص

⌔︙❬ .تدمير ❭ لحظر جميع اعضاء الجروب او القناه

⌔︙❬ .مسح الروابط ❭ ، ❬ .مسح الصور ❭ 

⌔︙❬ .مسح ❭ + كتابه العدد

⌔︙❬ .اضف جهاتي ❭

⌔︙❬ .اطردني ❭ لمغادره المجموعه ومسح بيناتها

⌔︙❬ .حذف صورة ❭ لحذف صوره الجروب

⌔︙❬ .ضع اسم ❭ + الاسم لوضع اسم للمجوعه
"""
txx3 = """
 اهلا بك عزيزي في اوامر اليوتيوب ⇊

⌔︙❬ .غ ❭ + كتابه اسم الاغنية 

⌔︙❬ .ف ❭ + كتابه اسم الفديو
"""
txx4 = """
 اهلا بك عزيزي في اوامر الاذاعه ⇊

⌔︙❬ .اذاعه خاص ❭ بالرد علي النص

⌔︙❬ .اذاعه للمجوعات ❭ بالرد علي النص

⌔︙❬ .اذاعه للقنوات ❭ بالرد علي النص

⌔︙❬ .توجيه للخاص ❭ بالرد علي النص

⌔︙❬ .توجيه للمجوعات ❭ بالرد علي النص

⌔︙❬ .توجيه للقنوات ❭ بالرد علي النص
"""
txx5 = """
 اهلا بك عزيزي في اوامر التسليه ⇊

⌔︙❬ .زواج ❭ ، ❬ .طلاق ❭ 

⌔︙❬ .مسح زوجاتي ❭

⌔︙❬ .رفع خول ❭ ، ❬ .تنزيل خول ❭

⌔︙❬ .مسح الخولات ❭

⌔︙❬ .رفع سيمب ❭ ، ❬ .تنزيل سيمب ❭ 

⌔︙❬ .رفع ابني ❭ ، ❬ .تنزيل ابني ❭ 

⌔︙❬ .مسح اولادي ❭

⌔︙❬ .رفع بنتي ❭ ، ❬ .تنزيل بنتي ❭ 

⌔︙❬ .مسح بناتي ❭ ، ❬ .مسح اولادي ❭ 

⌔︙❬ .رفع شاذ ❭ ، ❬ .تنزيل شاذ ❭

⌔︙❬ .رفع عرص ❭ ، ❬ .تنزيل عرص ❭  

⌔︙❬ .مسح الشواذ ❭ ، ❬ .مسح المعرصين ❭ 

⌔︙❬ .رفع كلب ❭ ، ❬ .تنزيل كلب ❭ 

⌔︙❬ .رفع متوحد ❭ ، ❬ .تنزيل متوحد ❭ 

⌔︙❬ .مسح الكلاب ❭ ، ❬ .مسح المتوحدين ❭ 

⌔︙❬ .رفع حمار ❭ ، ❬ .تنزيل حمار ❭

⌔︙❬ .رفع بقلبي ❭ ، ❬ .تنزيل بقلبي ❭ 

⌔︙❬ .مسح القلوب ❭ ، ❬ .مسح الحمير ❭
"""
txx6 = """


 اهلا بك عزيزي في اوامر اضافيه ⇊

⌔︙❬ .شرطه ❭ بالرد علي الشخص

⌔︙❬ .تهكير ❭ بالرد علي الشخص 

⌔︙❬ .قتل ❭ بالرد علي الشخص

⌔︙❬ .اقمار ❭ ، ❬ .قمور ❭ 

⌔︙❬ .مربع ❭ ، ❬ .دائره ❭ 

⌔︙❬ .يد ❭ ، ❬ .قياس ❭ 

⌔︙❬ .تحميل ❭

⌔︙❬ .بشره ❭ ، ❬ .العدد التنازلي ❭ 

⌔︙❬ .معاكسه ❭ ، ❬ .عبقري ❭ 

⌔︙❬ .افعي ❭ ، ❬ .الارض ❭

⌔︙❬ .ولد ❭ ، ❬ .مايكرو ❭  

⌔︙❬ .فايروس ❭ ، ❬ .نيكول ❭ 

⌔︙❬ .رسم ❭ ، ❬ .نجمه ❭ 

⌔︙❬ .مكعبات ❭ ، ❬ .مطر ❭ 

⌔︙❬ .تفريغ ❭ ، ❬ .النظام الشمسي ❭ 

⌔︙❬ .افكار ❭ ، ❬ .متت ❭

⌔︙❬ .زعلت ❭ ، ❬ .ساعه ❭ 

⌔︙❬ .مح ❭ ، ❬ .جيم ❭
"""



@bot.on_callback_query(filters.regex("^help1$"))
async def help1(client, callback_query):
  await callback_query.edit_message_text(txx1,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help2$"))
async def help2(client, callback_query):
  await callback_query.edit_message_text(txx2,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help3$"))
async def help3(client, callback_query):
  await callback_query.edit_message_text(txx3,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help4$"))
async def help4(client, callback_query):
  await callback_query.edit_message_text(txx4,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help5$"))
async def help5(client, callback_query):
  await callback_query.edit_message_text(txx5,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help6$"))
async def help6(client, callback_query):
  await callback_query.edit_message_text(txx6,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help$"))
async def back(client, callback_query):
  await callback_query.edit_message_text("⌔︙❬ م1 ❭ اوامر الخاص\n⌔︙❬ م2 ❭ اوامر القنوات والمجموعات\n⌔︙❬ م3 ❭ اوامر اليوتيوب\n⌔︙❬ م4 ❭ اوامر الاذاعه\n⌔︙❬ م5 ❭ اوامر التسليه\n⌔︙❬ م6 ❭ اوامر اضافيه",reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton(" م1",callback_data="help1"),
             InlineKeyboardButton(" م2",callback_data="help2"),
             ],
             [
             InlineKeyboardButton(" م3",callback_data="help3"),
             InlineKeyboardButton(" م4",callback_data="help4"),
             ],
             [
             InlineKeyboardButton(" م5",callback_data="help5"),
             InlineKeyboardButton(" م6",callback_data="help6"),
             ],
             [
             InlineKeyboardButton("◜𝗦َ𝗢َ𝗨َ𝗥َ𝗖َ𝗘 َِ𝐆 𝐀 𝐊◞",url="https://t.me/CU_FG"),
             ],
             [
             InlineKeyboardButton("𝐆 𝐀 𝐊 -",url="https://t.me/wvvwv3"),
             ]]
             ))

@bot.on_callback_query(filters.regex("^col/(.*?)") & filters.user(sudo_id))
async def get_color(c,msg):
    data = msg.data
    color = data.split("/")[1]
    reply_markup=InlineKeyboardMarkup([
       [InlineKeyboardButton("أعلي اليسار",callback_data="po/top-left"),InlineKeyboardButton("اعلي في المنتصف",callback_data="po/top-center"),InlineKeyboardButton("اعلي اليمين",callback_data="po/top-right")],
       [InlineKeyboardButton("يسار المنتصف",callback_data="po/middle-left"),InlineKeyboardButton("منتصف الصوره",callback_data="po/middle-center"),InlineKeyboardButton("يمين المنتصف",callback_data="po/middle-right")],
       [InlineKeyboardButton("أسفل اليسار",callback_data="po/bottom-left"),InlineKeyboardButton("اسفل في المنتصف",callback_data="po/bottom-center"),InlineKeyboardButton("اسفل اليمين",callback_data="po/bottom-right")],
    ])
    await msg.edit_message_text('• اختر موضع النص الان',reply_markup=reply_markup)
    r.set(f'{sudo_id}:user_color:{msg.from_user.id}',color)
    
@bot.on_callback_query(filters.regex("^po/(.*?)") & filters.user(sudo_id))
async def get_pos(c,msg):
    data = msg.data
    pos = data.split("/")[1]
    reply_markup=InlineKeyboardMarkup([
       [InlineKeyboardButton("كبير",callback_data="siz/40"),InlineKeyboardButton("متوسط",callback_data="siz/30"),InlineKeyboardButton("صغير",callback_data="siz/20")],
    ])
    await msg.edit_message_text('• اختر حجم النص الان',reply_markup=reply_markup)
    r.set(f'{sudo_id}:user_pos:{msg.from_user.id}',pos)

@bot.on_callback_query(filters.regex("^siz/(.*?)") & filters.user(sudo_id))
async def get_pos(c,msg):
    data = msg.data
    size = data.split("/")[1]
    pos = r.get(f'{sudo_id}:user_pos:{msg.from_user.id}')
    color = r.get(f'{sudo_id}:user_color:{msg.from_user.id}')
    text = r.get(f'{sudo_id}:user_text:{msg.from_user.id}')
    file = r.get(f'{sudo_id}:user_vid:{msg.from_user.id}')
    chat_id = r.get(f'{sudo_id}:user_chat:{msg.from_user.id}')
    await msg.edit_message_text('• جاري الكتابه علي الفيديو ...')
    typing = add_text_to_video(file, str(msg.from_user.id) + '.mp4',text,color,pos,size)
    if typing : 
        await msg.edit_message_text('• جاري الرفع ..')
        await app.send_animation(chat_id,typing,caption='By : @wvvwv3')
        remove(typing)
        await msg.edit_message_text('• تم كتابه {} علي المتحركه بنجاح ✅'.format(text))
    else :
        await message.edit('• حدث خطأ ! ')
    r.delete(f'{sudo_id}:user_pos:{msg.from_user.id}')
    r.delete(f'{sudo_id}:user_color:{msg.from_user.id}')
    r.delete(f'{sudo_id}:user_text:{msg.from_user.id}')
    r.delete(f'{sudo_id}:user_vid:{msg.from_user.id}')
    r.delete(f'{sudo_id}:user_chat:{msg.from_user.id}')
    remove(file)
