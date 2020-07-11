"""cmd .lol"""

from telethon import events
import io
import urllib.request
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.kang")
async def _(event):
    if event.fwd_from:
        return
    await event.edit("😂\n😂\n😂\n😂\n😂😂😂😂\n\n   😂😂😂\n 😂         😂\n😂           😂\n 😂         😂\n   😂😂😂\n\n😂\n😂\n😂\n😂\n😂😂😂😂")