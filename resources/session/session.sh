#!/usr/bin/env bash
# Arank - UserBot
# Copyright (C) 2021-2023 Mr_Mrs_Krishna
#
# This file is a part of < https://github.com/CoderXKrishna/Arank/ >
# PLease read the GNU Affero General Public License in <https://github.com/CoderXKrishna/Arank/blob/main/LICENSE/>.

clear
echo -e "\e[1m"
echo "  _                    _      "
echo " 	 / \   _ __ __ _ _ __ | | __"
echo "  / _ \ | '__/ _` | '_ \| |/ /"
echo " / ___ \| | | (_| | | | |   < "
echo " /_/   \_\_|  \__,_|_| |_|_\_\"
echo -e "\e[0m"                              
sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" # Don't Remove Dashes / Fix it
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/CoderXKrishna/Arank/main/resources/session/ssgen.py
pip uninstall telethon -y && install telethon
clear
python3 ssgen.py
