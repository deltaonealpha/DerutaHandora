"""cmd .lol"""

from telethon import events
import io
import urllib.request
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.kang")
async def _(args):
    if event.fwd_from:
        return
    await args.edit("😂\n😂\n😂\n😂\n😂😂😂😂\n\n   😂😂😂\n 😂         😂\n😂           😂\n 😂         😂\n   😂😂😂\n\n😂\n😂\n😂\n😂\n😂😂😂😂")
