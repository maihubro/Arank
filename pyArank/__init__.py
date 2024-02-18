# Arank - UserBot
# Copyright (C) 2021-2023 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/pyArank/blob/main/LICENSE>.

import os
import sys

from .version import __version__

run_as_module = __package__ in sys.argv or sys.argv[0] == "-m"


class ARAConfig:
    lang = "en"
    thumb = "resources/extras/Arank.jpg"


if run_as_module:
    import time

    from .configs import Var
    from .startup import *
    from .startup._database import ArankDB
    from .startup.BaseClient import ArankClient
    from .startup.connections import validate_session, vc_connection
    from .startup.funcs import _version_changes, autobot, enable_inline, update_envs
    from .version import Arank_version

    if not os.path.exists("./plugins"):
        LOGS.error(
            "'plugins' folder not found!\nMake sure that, you are on correct path."
        )
        exit()

    start_time = time.time()
    _ult_cache = {}
    _ignore_eval = []

    udB = ArankDB()
    update_envs()

    LOGS.info(f"Connecting to {udB.name}...")
    if udB.ping():
        LOGS.info(f"Connected to {udB.name} Successfully!")

    BOT_MODE = udB.get_key("BOTMODE")
    DUAL_MODE = udB.get_key("DUAL_MODE")

    USER_MODE = udB.get_key("USER_MODE")
    if USER_MODE:
        DUAL_MODE = False

    if BOT_MODE:
        if DUAL_MODE:
            udB.del_key("DUAL_MODE")
            DUAL_MODE = False
        Arank_bot = None

        if not udB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()
    else:
        Arank_bot = ArankClient(
            validate_session(Var.SESSION, LOGS),
            udB=udB,
            app_version=Arank_version,
            device_model="Arank",
        )
        Arank_bot.run_in_loop(autobot())

    if USER_MODE:
        asst = Arank_bot
    else:
        asst = ArankClient("asst", bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

    if BOT_MODE:
        Arank_bot = asst
        if udB.get_key("OWNER_ID"):
            try:
                Arank_bot.me = Arank_bot.run_in_loop(
                    Arank_bot.get_entity(udB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder and asst._bot:
        Arank_bot.run_in_loop(enable_inline(Arank_bot, asst.me.username))

    vcClient = vc_connection(udB, Arank_bot)

    _version_changes(udB)

    HNDLR = udB.get_key("HNDLR") or "."
    DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or HNDLR
else:
    print("pyArank 2022 © Mr_Mrs_Krishna")

    from logging import getLogger

    LOGS = getLogger("pyArank")

    Arank_bot = asst = udB = vcClient = None
