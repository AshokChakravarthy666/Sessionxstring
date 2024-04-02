from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/6f22d2d88f5b43ab9a805.jpg", caption=f"» ғɪꝛsᴛ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴏᴜꝛ ᴄʜᴧɴɴᴇʟ [𝖩𝖮𝖨𝖭]({link}) ᴧғᴛᴇꝛ ᴊᴏɪɴ sᴛᴧꝛᴛᴇᴅ ᴍᴇ ᴧɢᴧɪɴ !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴊᴏɪɴ", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ᴘꝛᴏᴍᴏᴛᴇ ᴍᴇ ᴧs ᴧɴ ᴧᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_ᴊᴏɪɴ ᴄʜᴧᴛ : {MUST_JOIN} !")
