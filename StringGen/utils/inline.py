from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="gensession")],
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="ᴍᴀ𝗌ᴛᴇʀ", url="https://t.me/FLEXDUB_OFFICIAL"
            ),
        ],
[
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ𝗌", url="https://t.me/FleX_Bots_News"),
            InlineKeyboardButton(
                text="ʙᴏᴛ𝗌", url="https://t.me/FLEXX_OFFICIAL"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
