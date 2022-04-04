
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from config import Config
from instaloader import Profile
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
import os
from utils import *

USER=Config.USER
OWNER=Config.OWNER
HOME_TEXT_OWNER=Config.HOME_TEXT_OWNER
HELP=Config.HELP
HOME_TEXT=Config.HOME_TEXT
session=f"./{USER}"
STATUS=Config.STATUS

insta = Config.L




@Client.on_message(filters.command("posts") & filters.private)
async def post(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id,
			disable_web_page_preview=True
        )
        return
    text=message.text
    username=USER
    if 1 not in STATUS:
        await message.reply_text("You Must Login First")
        return
    if " " in text:
        cmd, username = text.split(' ')
        profile = Profile.from_username(insta.context, username)
        is_followed = yes_or_no(profile.followed_by_viewer) 
        type = acc_type(profile.is_private)
        if type == "🔒Private🔒" and is_followed == "No":
            await message.reply_text("Sorry!\nI can't fetch details from that account.\nSince its a Private account and you are not following <code>@{username}</code>.")
            return
    await bot.send_message(
            message.from_user.id,
            f"What type of post do you want to download?.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Photos", callback_data=f"photos#{username}"),
                        InlineKeyboardButton("Videos", callback_data=f"video#{username}")
                    ]
                ]
            )
        )
    

@Client.on_message(filters.command("igtv") & filters.private)
async def igtv(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER),
            reply_markup=buttons,
			disable_web_page_preview=True
        )
        return
    text=message.text
    username=USER
    if 1 not in STATUS:
        await message.reply_text("You Must Login First")
        return
    if " " in text:
        cmd, username = text.split(' ')
        profile = Profile.from_username(insta.context, username)
        is_followed = yes_or_no(profile.followed_by_viewer) 
        type = acc_type(profile.is_private)
        if type == "🔒Private🔒" and is_followed == "No":
            await message.reply_text("Sorry!\nI can't fetch details from that account.\nSince its a Private account and you are not following <code>@{username}</code>.")
            return
    m=await message.reply_text(f"Fetching IGTV from <code>@{username}</code>")
    profile = Profile.from_username(insta.context, username)
    igtvcount = profile.igtvcount
    await m.edit(
        text = f"Do you Want to download all IGTV posts?\nThere are {igtvcount} posts.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Yes", callback_data=f"yesigtv#{username}"),
                    InlineKeyboardButton("No", callback_data=f"no#{username}")
                ]
            ]
        )
        )


@Client.on_message(filters.command("saved") & filters.private)
async def saved(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER),
            reply_markup=buttons,
			disable_web_page_preview=True
        )
        return
    text=message.text
    username=USER
    if 1 not in STATUS:
        await message.reply_text("you must login first")
        return
    count=None
    if " " in text:
        cmd, count = text.split(' ')
    m=await message.reply_text(f"Fetching your Saved Posts.")
    chat_id=message.from_user.id
    dir=f"{chat_id}/{username}"
    await m.edit("Starting Downloading..\nThis may take longer time Depending upon number of posts.")
    if count:
        command = [
            "instaloader",
            "--no-metadata-json",
            "--no-compress-json",
            "--no-profile-pic",
            "--no-posts",
            "--no-captions",
            "--no-video-thumbnails",
            "--login", USER,
            "-f", session,
            "--dirname-pattern", dir,
            ":saved",
            "--count", count
            ]
    else:
        command = [
            "instaloader",
            "--no-metadata-json",
            "--no-compress-json",
            "--no-profile-pic",
            "--no-posts",
            "--no-captions",
            "--no-video-thumbnails",
            "--login", USER,
            "-f", session,
            "--dirname-pattern", dir,
            ":saved"
            ]
    await download_insta(command, m, dir)
    await upload(m, bot, chat_id, dir)



@Client.on_message(filters.command("story") & filters.private)
async def story(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER),
            reply_markup=buttons,
			disable_web_page_preview=True
        )
        return
    text=message.text
    username=USER
    if 1 not in STATUS:
        await message.reply_text("you must login first ")
        return
    if " " in text:
        cmd, username = text.split(' ')
        profile = Profile.from_username(insta.context, username)
        is_followed = yes_or_no(profile.followed_by_viewer) 
        type = acc_type(profile.is_private)
        if type == "🔒Private🔒" and is_followed == "No":
            await message.reply_text("Sorry!\nI can't fetch details from that account.\nSince its a Private account and you are not following <code>@{username}</code>.")
            return
    m=await message.reply_text(f"Fetching stories of <code>@{username}</code>")
    chat_id=message.from_user.id
    dir=f"{chat_id}/{username}"
    await m.edit("Starting Downloading..\nThis may take longer time Depending upon number of posts.")
    command = [
        "instaloader",
        "--no-metadata-json",
        "--no-compress-json",
        "--no-profile-pic",
        "--no-posts",
        "--stories",
        "--no-captions",
        "--no-video-thumbnails",
        "--login", USER,
        "-f", session,
        "--dirname-pattern", dir,
        "--", username
        ]
    await download_insta(command, m, dir)
    await upload(m, bot, chat_id, dir)


@Client.on_message(filters.command("highlights") & filters.private)
async def highlights(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER),
            reply_markup=buttons,
			disable_web_page_preview=True
        )
        return
    username=USER
    if 1 not in STATUS:
        await message.reply_text("you must login first ")
        return
    text=message.text
    if " " in text:
        cmd, username = text.split(' ')
        profile = Profile.from_username(insta.context, username)
        is_followed = yes_or_no(profile.followed_by_viewer) 
        type = acc_type(profile.is_private)
        if type == "🔒Private🔒" and is_followed == "No":
            await message.reply_text("Sorry!\nI can't fetch details from that account.\nSince its a Private account and you are not following <code>@{username}</code>.")
            return
    m=await message.reply_text(f"Fetching highlights from profile <code>@{username}</code>")
    chat_id=message.from_user.id
    dir=f"{chat_id}/{username}"
    await m.edit("Starting Downloading..\nThis may take longer time Depending upon number of posts.")
    command = [
        "instaloader",
        "--no-metadata-json",
        "--no-compress-json",
        "--no-profile-pic",
        "--no-posts",
        "--highlights",
        "--no-captions",
        "--no-video-thumbnails",
        "--login", USER,
        "-f", session,
        "--dirname-pattern", dir,
        "--", username
        ]
    await download_insta(command, m, dir)
    await upload(m, bot, chat_id, dir)

