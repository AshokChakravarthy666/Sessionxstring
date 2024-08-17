from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
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
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config



ask_ques = "**» ᴄʜᴏᴏsᴇ ᴛʜᴇ sᴛꝛɪɴɢ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴧɴᴛ : :**"
buttons_ques = [
    [
        InlineKeyboardButton("ᴘʏꝛᴏɢꝛᴧᴍ", callback_data="pyrogram1"),
        InlineKeyboardButton("ᴘʏꝛᴏɢꝛᴧᴍ ᴠ2", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("ᴘʏꝛᴏɢꝛᴧᴍ ʙᴏᴛ", callback_data="pyrogram_bot"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛ", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text=" ɢᴇɴᴇꝛᴧᴛᴇ sᴛꝛɪɴɢ ", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "ᴛᴇʟᴇᴛʜᴏɴ"
    else:
        ty = "ᴘʏꝛᴏɢꝛᴧᴍ"
        if not old_pyro:
            ty += "ᴠ2"
    if is_bot:
        ty += " 𝖡𝖮𝖳"
    await msg.reply(f"» ᴛꝛʏɪɴɢ ᴛᴏ sᴛᴧꝛᴛ **{ty}** sᴇssɪᴏɴ ɢᴇɴᴇꝛᴧᴛᴏꝛ...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "ᴘʟᴇᴧsᴇ sᴇɴᴅ ʏᴏᴜꝛ **ᴧᴘɪ ɪᴅ** ᴛᴏ ᴘꝛᴏᴄᴇᴇᴅ.\n\nᴄʟɪᴄᴋ ᴏɴ  /skip ғᴏꝛ ᴜsɪɴɢ ʙᴏᴛ ᴧᴘɪ.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**ᴧᴘɪ ɪᴅ** ᴍᴜsᴛ ʙᴇ ᴧɴ ɪɴᴛᴇꝛɢᴇꝛ, sᴛᴧꝛᴛ ɢᴇɴᴇꝛᴧᴛɪɴɢ ʏᴏᴜꝛ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "» ɴᴏᴡ ᴘʟᴇᴧsᴇ sᴇɴᴅ ʏᴏᴜꝛ **ᴧᴘɪ_ʜᴧsʜ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "» ᴘʟᴇᴧsᴇ sᴇɴᴅ ʏᴏᴜꝛ **ᴘʜᴏɴᴇ ɴᴜᴍʙᴇꝛ** ᴡɪᴛʜ ᴄᴏᴜɴᴛꝛʏ ᴄᴏᴅᴇ ғᴏꝛ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴧɴᴛ ᴛᴏ ɢᴇɴᴇꝛᴧᴛᴇ sᴇssɪᴏɴ  \nᴇxᴧᴍᴘʟᴇ : `+910000000000`'"
    else:
        t = "ᴩʟᴇᴧsᴇ sᴇɴᴅ ʏᴏᴜꝛ **ʙᴏᴛ_ᴛᴏᴋᴇɴ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴧᴍᴩʟᴇ : `5432198765:abcdchampustringbot`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("» ᴛꝛʏɪɴɢ ᴛᴏ sᴇɴᴅ ᴏᴛᴩ ᴧᴛ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴜᴍʙᴇꝛ...")
    else:
        await msg.reply("» ᴛꝛʏɪɴɢ ᴛᴏ ʟᴏɢɪɴ ᴠɪᴧ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("» ʏᴏᴜꝛ **ᴧᴩɪ_ɪᴅ** ᴧɴᴅ **ᴧᴩɪ_ʜᴧsʜ** ᴄᴏᴍʙɪɴᴧᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴧᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢꝛᴧᴍ ᴧᴩᴩs sʏsᴛᴇᴍ. \n\nᴩʟᴇᴧsᴇ sᴛᴧꝛᴛ ɢᴇɴᴇꝛᴧᴛɪɴɢ ʏᴏᴜꝛ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("» ᴛʜᴇ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇꝛ** ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴧɴʏ ᴛᴇʟᴇɢꝛᴧᴍ ᴧᴄᴄᴏᴜɴᴛ.\n\nᴩʟᴇᴧsᴇ sᴛᴧꝛᴛ ɢᴇɴᴇꝛᴧᴛɪɴɢ ʏᴏᴜꝛ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "» ᴩʟᴇᴧsᴇ sᴇɴᴅ ᴛʜᴇ **ᴏᴛᴩ** ᴛʜᴧᴛ ʏᴏᴜ'ᴠᴇ ꝛᴇᴄᴇɪᴠᴇᴅ ғꝛᴏᴍ ᴛᴇʟᴇɢꝛᴧᴍ ᴏɴ ʏᴏᴜꝛ ᴧᴄᴄᴏᴜɴᴛ.\nɪғ ᴏᴛᴩ ɪs `12345`, **ᴩʟᴇᴧsᴇ sᴇɴᴅ ɪᴛ ᴧs** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ꝛᴇᴧᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴧsᴇ sᴛᴧꝛᴛ ɢᴇɴᴇꝛᴧᴛɪɴɢ ʏᴏᴜꝛ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡꝛᴏɴɢ.**\n\nᴩʟᴇᴧsᴇ sᴛᴧꝛᴛ ɢᴇɴᴇꝛᴧᴛɪɴɢ ʏᴏᴜꝛ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪꝛᴇᴅ.**\n\nᴩʟᴇᴧsᴇ sᴛᴧꝛᴛ ɢᴇɴᴇꝛᴧᴛɪɴɢ ʏᴏᴜꝛ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "» ᴩʟᴇᴧsᴇ ᴇɴᴛᴇꝛ ʏᴏᴜꝛ **ᴛᴡᴏ sᴛᴇᴩ ᴠᴇꝛɪғɪᴄᴧᴛɪᴏɴ** ᴩᴧssᴡᴏꝛᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ꝛᴇᴧᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴧsᴇ sᴛᴧꝛᴛ ɢᴇɴᴇꝛᴧᴛɪɴɢ ʏᴏᴜꝛ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("» ᴛʜᴇ ᴩᴧssᴡᴏꝛᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡꝛᴏɴɢ.\n\nᴩʟᴇᴧsᴇ sᴛᴧꝛᴛ ɢᴇɴᴇꝛᴧᴛɪɴɢ ʏᴏᴜꝛ sᴇssɪᴏɴ ᴧɢᴧɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**ᴛʜɪs ɪs ʏᴏᴜꝛ {ty} sᴛꝛɪɴɢ sᴇssɪᴏɴ** \n\n`{string_session}` \n\n**ɢᴇɴᴇꝛᴧᴛᴇᴅ ʙʏ :** @TheChampu\n🍒 **ɴᴏᴛᴇ :** ᴅᴏɴᴛ sʜᴧꝛᴇ ᴡɪᴛʜ ᴧɴʏᴏɴᴇ ʙᴇᴄᴧᴜsᴇ ʜᴇ ᴄᴧɴ ʜᴧᴄᴋ ʏᴏᴜꝛ ᴧʟʟ ᴅᴧᴛᴧ. 🍑 ᴅᴏɴᴛ ғᴏꝛɢᴇᴛ ᴛᴏ ᴊᴏɪɴ @akaChampu & @TheChampu 🥺"
    try:
        if not is_bot:
            await bot.send_message(msg.chat.id, text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "» sᴜᴄᴄᴇssғᴜʟʟʏ ɢᴇɴᴇꝛᴧᴛᴇᴅ ʏᴏᴜꝛ {} sᴛꝛɪɴɢ sᴇssɪᴏɴ.\n\nᴘʟᴇᴧsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜꝛ sᴧᴠᴇᴅ ᴍᴇssᴧɢᴇ ᴛᴏ ɢᴇᴛ ɪᴛ ! \n\nᴧ sᴛꝛɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇꝛᴧᴛᴏꝛ ʙᴏᴛ ʙʏ @TheChampu ♦".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏꝛᴏɢꝛᴧᴍ"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**» ᴄᴧɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛꝛɪɴɢ ɢᴇɴᴇꝛᴧᴛɪᴏɴ ᴩꝛᴏᴄᴇss !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**» sᴜᴄᴄᴇssғᴜʟʟʏ ꝛᴇsᴛᴧꝛᴛᴇᴅ ᴛʜɪs ʙᴏᴛ ғᴏꝛ ʏᴏᴜ !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**» ᴄᴧɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛꝛɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇꝛᴧᴛɪɴɢ ᴘꝛᴏᴄᴇss !**", quote=True)
        return True
    else:
        return False
