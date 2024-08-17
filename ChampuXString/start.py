from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""ʜᴇʟʟᴏ {msg.from_user.mention},

✨ ɪɴᴛꝛᴏᴅᴜᴄɪɴɢ {me2} - ᴛʜᴇ ᴇɴɪɢᴍᴧᴛɪᴄ sᴛꝛɪɴɢ ɢᴇɴᴇꝛᴧᴛᴏꝛ ʙᴏᴛ! ✨
🔐 ᴜɴʟᴏᴄᴋ ᴛʜᴇ ᴍʏsᴛᴇꝛɪᴇs ᴏғ sᴛꝛɪɴɢ ɢᴇɴᴇꝛᴧᴛɪᴏɴ!
🌌 sʟᴇᴇᴋ. ᴇʟᴇɢᴧɴᴛ. ᴛɪᴍᴇʟᴇss.

🎨 ᴄꝛᴇᴧᴛᴇᴅ ʙʏ: [ᴄʜᴧᴍᴘᴜ](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ɢᴇɴᴇʀᴧᴛᴇ sᴛʀɪɴɢ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/akaChampu"),
                    InlineKeyboardButton("ᴄʜᴧɴɴᴇʟ", url="https://t.me/TheChampu")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
