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

✨ ɪɴᴛʀᴏᴅᴜᴄɪɴɢ {me2} - ᴛʜᴇ ᴇɴɪɢᴍᴧᴛɪᴄ sᴛʀɪɴɢ ɢᴇɴᴇʀᴧᴛᴏʀ ʙᴏᴛ! ✨
🔐 ᴜɴʟᴏᴄᴋ ᴛʜᴇ ᴍʏsᴛᴇʀɪᴇs ᴏғ sᴛʀɪɴɢ ɢᴇɴᴇʀᴧᴛɪᴏɴ!
🌌 sʟᴇᴇᴋ. ᴇʟᴇɢᴧɴᴛ. ᴛɪᴍᴇʟᴇss.

🎨 ᴄʀᴇᴧᴛᴇᴅ ʙʏ: [𝙰𝚂𝙷𝙾𝙺𝚇𝙶𝙷𝙾𝚂𝚃](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ɢᴇɴᴇʀᴧᴛᴇ sᴛʀɪɴɢ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/+ITKJ6qtpM0hiOGU9"),
                    InlineKeyboardButton("ᴄʜᴧɴɴᴇʟ", url="https://t.me/+HMHH1y96Sz1jMmVl")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
