#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from YousefMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["ميوزك", "الميوزك", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/65ae4f8eed3deb620852b.jpg",
        caption=f"""<b>» مرحبـاً بك عـزيـزي </b> {message.from_user.mention} .\n\n<b>» استخـدم الازرار بالاسفـل \n» لـ تصفـح اوامـر سورس ⁷⁷𝒏𝒂𝒋𝒅 🇸🇦</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " اوامــر التشغيــل ", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        " اوامـر القنـاة ", callback_data="zzzch"),
                    InlineKeyboardButton(
                       " اوامـر الادمـن ", callback_data="zzzad"),
                ],[ 
                    InlineKeyboardButton(
                        "𝐬𝐨𝐮𝐫𝐜𝐞 𝐚𝐥𝐢𝐜𝐞", url="https://t.me/ngd_1") 
                ],[
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"), 
                ],
            ]
        ),
    )


