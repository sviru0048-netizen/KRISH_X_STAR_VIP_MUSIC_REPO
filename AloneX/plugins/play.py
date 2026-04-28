@app.on_message(
    filters.command(["play", "playforce", "vplay", "vplayforce"])
    & filters.group
    & ~app.bl_users
)
@lang.language()
@checkUB
async def play_hndlr(
    _,
    m: types.Message,
    force: bool = False,
    m3u8: bool = False,
    video: bool = False,
    url: str = None,
) -> None:

    sent = await m.reply_text("🔍 **Searching Your Song...**")

    mention = m.from_user.mention
    media = tg.get_media(m.reply_to_message) if m.reply_to_message else None
    tracks = []

    # 🔎 SEARCH PART
    if len(m.command) >= 2:
        query = " ".join(m.command[1:])
        file = await yt.search(query, sent.id, video=video)
    elif media:
        setattr(sent, "lang", m.lang)
        file = await tg.download(m.reply_to_message, sent)
    else:
        return await sent.edit_text("❌ **Use:** /play song name")

    if not file:
        return await sent.edit_text("❌ **Song Not Found!**")

    # ⏱ LIMIT CHECK
    if file.duration_sec > config.DURATION_LIMIT:
        return await sent.edit_text(
            f"⏱ **Max Duration:** {config.DURATION_LIMIT // 60} min only!"
        )

    # 📥 ADD TO QUEUE
    position = queue.add(m.chat.id, file)

    # 🎶 IF ALREADY PLAYING
    if position != 0 or await db.get_call(m.chat.id):
        return await sent.edit_text(
            f"""
╔══❖ 🎧 **SONG QUEUED** ❖══╗

🎵 **Title:** [{file.title}]({file.url})  
⏱ **Duration:** {file.duration}  
👤 **Requested By:** {mention}  

📌 **Position:** {position}

╚══❖ 💎 KRISH X STAR ❖══╝
""",
            reply_markup=types.InlineKeyboardMarkup(
                [
                    [
                        types.InlineKeyboardButton(
                            "▶️ Play Now", callback_data="play_now"
                        ),
                        types.InlineKeyboardButton(
                            "📜 Queue", callback_data="queue"
                        ),
                    ]
                ]
            ),
        )

    # ⬇️ DOWNLOAD
    if not file.file_path:
        await sent.edit_text("⬇️ **Downloading Song...**")
        file.file_path = await yt.download(file.id, video=video)

    # ▶️ PLAY
    await anon.play_media(chat_id=m.chat.id, message=sent, media=file)

    # 🎧 NOW PLAYING MESSAGE
    await sent.edit_text(
        f"""
╔══❖ 🔥 **NOW PLAYING** 🔥 ❖══╗

🎵 **Title:** [{file.title}]({file.url})  
⏱ **Duration:** {file.duration}  
👤 **Requested By:** {mention}  

⚡ **Powered By KRISH X STAR**

╚══❖ 🚀 Enjoy Music ❖══╝
""",
        reply_markup=types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton("⏸ Pause", callback_data="pause"),
                    types.InlineKeyboardButton("⏭ Skip", callback_data="skip"),
                ],
                [
                    types.InlineKeyboardButton("🛑 Stop", callback_data="stop"),
                    types.InlineKeyboardButton("📜 Queue", callback_data="queue"),
                ],
            ]
        ),
    )
