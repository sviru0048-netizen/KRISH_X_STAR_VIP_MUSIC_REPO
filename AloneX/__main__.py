# Copyright (c) 2025 KRISH STAR
# Licensed under the MIT License.
# This file is part of KRISH STAR MUSIC BOT

import asyncio
import importlib

from pyrogram import idle

from AloneX import (anon, app, config, db,
                   logger, stop, userbot, yt)
from AloneX.plugins import all_modules


async def main():
    logger.info("🚀 KRISH STAR MUSIC BOT STARTING...")

    await db.connect()
    await app.boot()
    await userbot.boot()
    await anon.boot()

    logger.info("✅ KRISH STAR BOT CONNECTED SUCCESSFULLY!")

    for module in all_modules:
        importlib.import_module(f"AloneX.plugins.{module}")

    logger.info(f"🔥 KRISH STAR BOT: Loaded {len(all_modules)} modules.")

    if config.COOKIES_URL:
        await yt.save_cookies(config.COOKIES_URL)
        logger.info("🍪 KRISH STAR: Cookies Loaded Successfully!")

    sudoers = await db.get_sudoers()
    app.sudoers.update(sudoers)
    app.bl_users.update(await db.get_blacklisted())

    logger.info(f"👑 KRISH STAR BOT: Loaded {len(app.sudoers)} sudo users.")

    logger.info("🎵 KRISH STAR MUSIC BOT IS NOW RUNNING...")

    await idle()

    logger.info("🛑 KRISH STAR BOT STOPPING...")
    await stop()


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        logger.info("❌ KRISH STAR BOT STOPPED BY USER")
