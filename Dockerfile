# Arank - UserBot
# Copyright (C) 2021-2023 TeamArank
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in <https://github.com/CoderXKrishna/Arank/blob/main/LICENSE/>.

FROM CoderXKrishna/Arank:main

# set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/CoderXKrishna"

# start the bot.
CMD ["bash", "startup"]
