# Arank - UserBot
# Copyright (C) 2021-2023 TeamArank
#
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/Arank/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, Arank_cmd

REPOMSG = """
• **Arank USERBOT** •\n
• Repo - [Click Here](https://github.com/CoderXKrishna/Arank)
• Addons - [Click Here](https://github.com/CoderXKrishna/ArankAddons)
• Support - @Carding_Chronicle
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/CoderXKrishna/Arank"),
        Button.url("Addons", "https://github.com/CoderXKrishna/ArankAddons"),
    ],
    [Button.url("Support Group", "t.me/Carding_Chronicle")],
]

ULTSTRING = """🎇 **Thanks for Deploying Arank Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@Arank_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@Arank_cmd(pattern="Arank$")
async def useArank(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/0b9d7bd278272147f1f3c.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
