import telebot
import random
import messagesBots

@bot.message_handler(commands=["almortagel"])
def startt(message):
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
        voicerurl = "https://t.me/EIEI06/" + str(random.randint(24, 618))
        bot.send_voice(message.chat.id, voicerurl, caption="« صلي على سيدنا محمد ﷺ »", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
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
        voicer_url = "https://t.me/yoipopl/" + str(random.randint(2, 140))
        bot.send_voice(message.chat.id, voicer_url, caption="🥹♥ ¦ تـم اختيـار استوري لـك", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton('✧ - المطور 🌐', url='https://t.me/Almortagel_12'),
            telebot.types.InlineKeyboardButton('✧ - قناة مطور البوت', url='https://t.me/AlmortagelTech')
@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    if text == "نقشبندي" or text == "الشيخ نقشبندي":
        voiceurl = "https://t.me/ggcnjj/" + str(random.randint(2, 114))
        bot.send_voice(message.chat.id, voiceurl, caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لـك", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
            telebot.types.InlineKeyboardButton('✧ - المطور 🌐', url='https://t.me/Almortagel_12'),
            telebot.types.InlineKeyboardButton('✧ - قناة مطور البوت', url='https://t.me/AlmortagelTech')            

@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    if text == "افاتار شباب" or text == "صور شباب":
        voiceee_url = "https://t.me/vgbmm/" + str(random.randint(2, 148))
        bot.send_photo(message.chat.id, voiceee_url, caption="🥹♥ ¦ تـم اختيـار افاتار شباب لـك", reply_to_message_id=message.message_id, reply_markup=telebot.types.InlineKeyboardMarkup().row(
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