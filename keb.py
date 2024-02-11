import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

#كسمك تحياتي😂
REPLY_MESSAGE = "**🧑🏻‍✈️︙اهلا بك بك عزيزي العضو ♥️**\n**⤵️︙ اليـكـ كيب الاعضاء الخاص بسورس المرتجل**"

REPLY_MESSAGE_BUTTONS = [
    [
             ("المبرمج"),                   
             ("سورس")

          ],
          [
             ("لو خيروك"),
             ("كت تويت") 
          ],
          [
             ("اذكار"),
             ("صراحه") 
          ],
          [
             ("افاتار شباب"),
             ("افاتار بنات") 
          ],
          [
             ("استوري"),
              ("متحركه")
          ],
          [
             ("قران"),
              ("نقشبندي")
          ],
          [
              ("عبدالباسط"),
              ("تلاوات")
          ],
          [
             ("غنيلي"),
             ("سوال")         
          ],
          [
             ("الالعاب"),
             ("انمي")
          ],
          [
             ("اقتباس"),
             ("هيدرات")
          ],
          [           
        ("❎ ¦ حذف الكيبورد")
    ]
]

@app.on_message(filters.command(["/almortagel"], "") & filters.private)
async def madison(client: Client, message: Message): 
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


@app.on_message(filters.command("❎ ¦ حذف الكيبورد") 
& filters.private
)
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.command(["صوره", "🕷", "صورهه", "صور"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار صوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )


@app.on_message(filters.command(["انميي", "انمي"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(3,153)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار انمي لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )


@app.on_message(filters.command(["متحركه. 🎬", "متحركه"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,926)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="💙 ¦ تـم اختيـار ملصق لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["تلاوات", "تلاوة"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(24,618)
    url = f"https://t.me/EIEI06/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار تلاوة قرآنيه لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["اقتباسات", "اقتباس"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(3,102)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار اقتباس لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["هيدرا", "هيدرات"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,153)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار هيدرات لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["صور", "افاتار بنات"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,216)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار افاتار بنات لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["صور شباب", "افاتار شباب"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,148)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار افاتار شباب لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["سوره", "قران"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,82)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار ايـه قرآنيه لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["الشيخ", "النقشبندي", "نقشبندي"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,114)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["عبدالباسط", "عبدالباسط عبدالصمد"], "")
& filters.group
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(7,265)
    url = f"https://t.me/telawatnader/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ عبدالباسط لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["استوري", "استوريهات. 🥹"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,148)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id,url,caption="💚 ¦ تـم اختيـار استوري لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )



@app.on_message(filters.command("🍁 ¦ حظر") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5dc0bab3462bd868b3081.jpg",
        caption=f"""• اليك طريقه حظر اي شخص .\n\n• قم بـ استخدام الامر هكذا : /block حظر ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🖇 ¦ الغاء حظر") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4268ef332d710c5547357.jpg",
        caption=f"""• اليك طريقه الغاء حظر شخص .\n\n• قم بـ استخدام الامر هكذا : /unblock الغاء حظر ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🔥 ¦ المحظورين عام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cc2b0b6c4eea77c43b8b4.jpg",
        caption=f"""• اليك طريقه معرفه المحظورين عام .\n\n• قم بـ استخدام الامر هكذا : /blockedusers المحظورين ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🗞 ¦ حظر عام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d0db8351713f77bb8450b.jpg",
        caption=f"""• اليك طريقه الحظر العام .\n\n• قم بـ استخدام الامر هكذا :/ح ع\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🔖 ¦ الغاء العام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/611ee77edc1763ea2b07b.jpg",
        caption=f"""• اليك طريقه الغاء الحظر العام .\n\n• قم بـ استخدام الامر هكذا : /unblock الغاء حظر ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🪂 ¦ الاحصائيات") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/571e1fb1857c8ae6e6be1.jpg",
        caption=f"""• اليك طريقه معرفه الاحصائيات .\n\n• قم بـ استخدام الامر هكذا : الاحصائيات\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("ذكاء الاصطناعي") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c544b771eeed7dbdc51a9.jpg",
        caption=f"""• اليك طريقه معرفه سرعه البوت .\n\n• قم بـ استخدام الامر هكذا : /gpt\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )