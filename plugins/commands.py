

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from config import Config
import asyncio
import sys
import os

USER=Config.USER
OWNER=Config.OWNER
HOME_TEXT=Config.HOME_TEXT
HOME_TEXT_OWNER=Config.HOME_TEXT_OWNER
HELP=Config.HELP


@Client.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
	if str(cmd.from_user.id) != OWNER:	
		await cmd.reply_text(
			HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id,
			)
		)
	else:
		await cmd.reply_text(
			HOME_TEXT_OWNER.format(cmd.from_user.first_name, cmd.from_user.id), 
			disable_web_page_preview=True,
			)

@Client.on_message(filters.command("restart") & filters.private)
async def stop(bot, cmd):
	if str(cmd.from_user.id) != OWNER:	
		await cmd.reply_text(
			HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id,
			)
		)
		return
	msg = await bot.send_message(
		text="Restarting your bot..",
		chat_id=cmd.from_user.id
		)
	await asyncio.sleep(2)
	await msg.edit("All Processes Stopped and Restarted")
	os.execl(sys.executable, sys.executable, *sys.argv)