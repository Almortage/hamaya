from telebot import *
from telebot.types import *
from time import sleep, time
from database_main import *

# from keepAlive import keep_alive


import telebot, time
from time import time
from telebot import types
from functions_to_my_bots import *
import messagesBots


def send_member_private(message: types.Message):
    global cv, vc
    mtxt = message.text
    CHid = message.from_user.id
            if mtxt == "/almortagel":
            bot.send_message(
                message.chat.id,
                text=messagesBots.message_for_admin,
                parse_mode="HTML",
                reply_to_message_id=message.id,
                reply_markup=mycommands_on(),
            )
    mrk = ReplyKeyboardMarkup(row_width=6)

    ttns = [
        KeyboardButton("تلاوات"),
        KeyboardButton("عبد الباسط"),
        ]
    stns = [
        KeyboardButton(text="نقشبندي"),
        KeyboardButton(text="استوري"),
        ],
    ttnns = [
        KeyboardButton(text="افاتار شباب"),
        KeyboardButton(text="افاتار بنات"),
    ]
    mrk.add(*ttns)
    mrk.add(*stns)
    mrk.add(*ttnns)
    return mrk
    
@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    if text == "تلاو" or text == "تلاوات" or text == "تلاوة":
        voice_url = "https://t.me/EIEI06/" + str(random.randint(24, 618))
        bot.send_voice(message.chat.id, voice_url, caption="« صلي على سيدنا محمد ﷺ »", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton('✧ - المطور 🌐', url='https://t.me/Almortagel_12'),
            telebot.types.InlineKeyboardButton('✧ - قناة مطور البوت', url='https://t.me/AlmortagelTech')
@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    if text == "عبدالباسط":
        voice_url = "https://t.me/telawatnader/" + str(random.randint(7, 265))
        bot.send_voice(message.chat.id, voice_url, caption="🥹♥ ¦ تـم اختيـار الشيخ عبدالباسط لـك", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton('✧ - المطور 🌐', url='https://t.me/Almortagel_12'),
            telebot.types.InlineKeyboardButton('✧ - قناة مطور البوت', url='https://t.me/AlmortagelTech')
@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    if text == "استوري" or text == "استوريات":
        voice_url = "https://t.me/yoipopl/" + str(random.randint(2, 140))
        bot.send_voice(message.chat.id, voice_url, caption="🥹♥ ¦ تـم اختيـار استوري لـك", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton('✧ - المطور 🌐', url='https://t.me/Almortagel_12'),
            telebot.types.InlineKeyboardButton('✧ - قناة مطور البوت', url='https://t.me/AlmortagelTech')
@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    if text == "نقشبندي" or text == "الشيخ نقشبندي":
        voice_url = "https://t.me/ggcnjj/" + str(random.randint(2, 114))
        bot.send_voice(message.chat.id, voice_url, caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لـك", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton('✧ - المطور 🌐', url='https://t.me/Almortagel_12'),
            telebot.types.InlineKeyboardButton('✧ - قناة مطور البوت', url='https://t.me/AlmortagelTech')            

@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    if text == "افاتار شباب" or text == "صور شباب":
        voicee_url = "https://t.me/vgbmm/" + str(random.randint(2, 148))
        bot.send_photo(message.chat.id, voicee_url, caption="🥹♥ ¦ تـم اختيـار افاتار شباب لـك", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton('✧ - المطور 🌐', url='https://t.me/Almortagel_12'),
            telebot.types.InlineKeyboardButton('✧ - قناة مطور البوت', url='https://t.me/AlmortagelTech') 
@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    if text == "افاتار بنات" or text == "صور بنات":
        voicee_url = "https://t.me/vvyuol/" + str(random.randint(2, 216))
        bot.send_photo(message.chat.id, voicee_url, caption="🥹♥ ¦ تـم اختيـار افاتار بنات لـك", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton('✧ - المطور 🌐', url='https://t.me/Almortagel_12'),
            telebot.types.InlineKeyboardButton('✧ - قناة مطور البوت', url='https://t.me/AlmortagelTech') 
            