# Arank - UserBot
# Copyright (C) 2021-2023 TeamArank
#
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/Arank/blob/main/LICENSE/>.

from telethon import Button, custom

from plugins import ATRA_COL, InlinePlugin
from pyArank import *
from pyArank import _ult_cache
from pyArank._misc import owner_and_sudos
from pyArank._misc._assistant import asst_cmd, callback, in_pattern
from pyArank.fns.helper import *
from pyArank.fns.tools import get_stored_file
from strings import get_languages, get_string

OWNER_NAME = Arank_bot.full_name
OWNER_ID = Arank_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException as er:
        LOGS.exception(er)
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
