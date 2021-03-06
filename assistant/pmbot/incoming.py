# Ultroid - UserBot
# Copyright (C) 2020 ULTROID-OP
#
# This file is a part of < https://github.com/ULTROID-OP/ULTROID-BOT/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ULTROID-OP/Ultroid/blob/main/LICENSE/>.

# https://github.com/LEGENDX22/TeleBot/blob/master/telebot/plugins/mybot/pmbot/incoming.py
"""
Incoming Message(s) forwarder.
"""

from telethon import events

from . import *

# if incoming


@asst.on(events.NewMessage(func=lambda e: e.is_private))
async def on_new_mssg(event):
    incoming = event.raw_text
    who = event.sender_id
    if is_blacklisted(who):
        return
    # doesn't reply to that user anymore
    if incoming.startswith("/"):
        pass
    elif who == OWNER_ID:
        return
    else:
        await event.forward_to(OWNER_ID)
