# Arank - UserBot
# Copyright (C) 2021-2023 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/Arank/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """🎇 **Thanks for Deploying Arank Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage.""",
    2: """🎉** About Arank**

🧿 Arank is Pluggable and powerful Telethon Userbot, made in Python from Scratch. It is Aimed to Increase Security along with Addition of Other Useful Features.

❣ Made by **@Mr_Mrs_Krishna**""",
    3: """**💡• FAQs •**

-> [Username Tracker](https://t.me/Mr_Mrs_Krishna/24)
-> [Keeping Custom Addons Repo](https://t.me/Mr_Mrs_Krishna/28)
-> [Disabling Deploy message](https://t.me/Mr_Mrs_Krishna/27)
-> [Setting up TimeZone](https://t.me/Mr_Mrs_Krishna/22)
-> [About Inline PmPermit](https://t.me/Mr_Mrs_Krishna/21)
-> [About Dual Mode](https://t.me/Mr_Mrs_Krishna/18)
-> [Custom Thumbnail](https://t.me/Mr_Mrs_Krishna/13)
-> [About FullSudo](https://t.me/Mr_Mrs_Krishna/11)
-> [Setting Up PmBot](https://t.me/Mr_Mrs_Krishna/2)
-> [Also Check](https://t.me/Mr_Mrs_Krishna/14)

**• To Know About Updates**
  - Join @Mr_Mrs_Krishna.""",
    4: f"""• `To Know All Available Commands`

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """• **For Any Other Query or Suggestion**
  - Move to **@ArankSupportChat**.

• Thanks for Reaching till END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_4"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_2"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )
