# Bot
from pyrogram.raw import functions, types
from pyrogram import Client, idle
from pyromod import listen
from config import Config
STATUS=Config.STATUS

USER=Config.USER
bot = Client(
    "Instagrambot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    workers=50,
    plugins=dict(root="plugins")
    )


async def main():
    async with bot:
        await bot.download_media(Config.INSTA_SESSIONFILE_ID, file_name=f"./{Config.USER}")
        Config.L.load_session_from_file(USER, filename=f"./{USER}")
        STATUS.add(1)

if Config.INSTA_SESSIONFILE_ID:
    bot.run(main())

bot.start()

idle()
bot.stop()
