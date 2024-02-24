# Arank - UserBot
# Copyright (C) 2021-2023 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/CoderXKrishna/pyArank/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    )
    SESSION = "1BJWap1wBu2HtBIqUi8zD04CqP50QO4vf5-Zy5krlkYHj8YZAQy4ePf2hIkTQNX3qDeNbFRGDCwSCo0LCK4Ddoc1lSfoJAru4XfUM78dc3aSVn-TDyVQY5MOvFYQpY1NEaDzYxdoE997bRbjbSlymrh1rWT9oSkQumZV7AceGzs-drvAu1udwKOHWboJUoMA7Qm_LvlKwIqpRFWpGhO17RksD9wmdFfbvlNtFP41H2mCD7j-78bR91qZd04cmbtrYG9GhqswXVwSWmhBOdQV7HAwVQvj1d3Pmzz6-vO8vUoS4w0iBVlA3r4QDBABAOUEswACk9pi6bH-BO06iV5nAndkEDvbj_uY="
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default=None)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
