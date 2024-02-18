# Arank - UserBot
# Copyright (C) 2021-2023 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/Arank/blob/main/LICENSE/>.

import asyncio
import os
import time
from random import choice

import requests
from telethon import Button, events
from telethon.tl import functions, types  # pylint:ignore

from pyArank import *
from pyArank._misc._assistant import asst_cmd, callback, in_pattern
from pyArank._misc._decorators import Arank_cmd
from pyArank._misc._wrappers import eod, eor
from pyArank.dB import DEVLIST, Arank_IMAGES
from pyArank.fns.helper import *
from pyArank.fns.misc import *
from pyArank.fns.tools import *
from pyArank.startup._database import _BaseDatabase as Database
from pyArank.version import __version__, Arank_version
from strings import get_help, get_string

udB: Database

Redis = udB.get_key
con = TgConverter
quotly = Quotly()
OWNER_NAME = Arank_bot.full_name
OWNER_ID = Arank_bot.uid

Arank_bot: ArankClient
asst: ArankClient

LOG_CHANNEL = udB.get_key("LOG_CHANNEL")


def inline_pic():
    INLINE_PIC = udB.get_key("INLINE_PIC")
    if INLINE_PIC is None:
        INLINE_PIC = choice(Arank_IMAGES)
    elif INLINE_PIC == False:
        INLINE_PIC = None
    return INLINE_PIC


Telegraph = telegraph_client()

List = []
Dict = {}
InlinePlugin = {}
N = 0
cmd = Arank_cmd
STUFF = {}

# Chats, which needs to be ignore for some cases
# Considerably, there can be many
# Feel Free to Add Any other...

NOSPAM_CHAT = [
    -1001994490527,  # ArankSupportChat
    -1001994490527,  # PyrogramChat
    -1001994490527,  # TelethonChat
    -1001994490527,  # Python
    -1001994490527,  # DurovsChat
    -1001994490527,  # SharingUserbot
]

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]

ATRA_COL = [
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "Cyan",
    "LightSkyBlue",
    "Turquoise",
    "MediumVioletRed",
    "Aquamarine",
    "Lightcyan",
    "Azure",
    "Moccasin",
    "PowderBlue",
]
