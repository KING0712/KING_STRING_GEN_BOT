from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="🖤 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐄𝐒𝐒𝐈𝐎𝐍 🖤", callback_data="gensession")],
        [
            [InlineKeyboardButton(text="🖤 𝐎𝐖𝐍𝐄𝐑 🖤", url="https://t.me/l_MR_ll_KING_l"],
            InlineKeyboardButton(
                text="", url=""
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
