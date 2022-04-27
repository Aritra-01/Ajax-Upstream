"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "You are not dead. You are still here. You have no love for me now. Well, you're not changed..😔 Sometimes but nothing /start Do it and see..🙂" 
UNMESH = "<b>উন্মেষ Channel LINK ›› https://t.me/HoiChoiTvAddaa</b>"
CHANNEL = "<b>জলতরঙ্গ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b> ›› https://t.me/Joltorongo\n\n<b>𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/HoiChoiTvAddaa</b>\n\n<b>GROUP ›› https://t.me/HoiChoi_Group</b>"
JOLTORONGO = "<b>জলতরঙ্গ link ›› <a href=https://t.me/Joltorongo</a></b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("unmesh", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(UNMESH)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("joltorongo", COMMAND_HAND_LER) & f_onw_fliter)
async def joltorongo(_, message):
    await message.reply_text(JOLTORONGO)


