<h2 align="center">
    𝄟🌹Arank UserBot🌹​​​​​𝄟​​​​​
</h2>

<p align="center">
  <img src="https://telegra.ph/file/0b9d7bd278272147f1f3c.jpg">
</p>
<h1 align="center">
  <b>Arank - UserBot</b>
</h1>

<b>A stable pluggable Telegram userbot + Voice & Video Call music bot, based on Telethon.</b>

[![](https://img.shields.io/badge/Arank-v0.8-crimson)](#)
[![Stars](https://img.shields.io/github/stars/CoderXKrishna/Arank?style=flat-square&color=yellow)](https://github.com/CoderXKrishna/Arank/stargazers)
[![Forks](https://img.shields.io/github/forks/CoderXKrishna/Arank?style=flat-square&color=orange)](https://github.com/CoderXKrishna/Arank/fork)
[![Size](https://img.shields.io/github/repo-size/CoderXKrishna/Arank?style=flat-square&color=green)](https://github.com/CoderXKrishna/Arank/)   
[![Python](https://img.shields.io/badge/Python-v3.10.3-blue)](https://www.python.org/)
[![CodeFactor](https://www.codefactor.io/repository/github/CoderXKrishna/Arank/badge/main)](https://www.codefactor.io/repository/github/CoderXKrishna/Arank/overview/main)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/CoderXKrishna/Arank/graphs/commit-activity)
[![Docker Pulls](https://img.shields.io/docker/pulls/theCoderXKrishna/Arank?style=flat-square)](https://img.shields.io/docker/pulls/theCoderXKrishna/Arank?style=flat-square)   
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/CoderXKrishna/Arank)
[![Contributors](https://img.shields.io/github/contributors/CoderXKrishna/Arank?style=flat-square&color=green)](https://github.com/CoderXKrishna/Arank/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/CoderXKrishna/Arank/blob/main/LICENSE)   
[![Sparkline](https://stars.medv.io/CoderXKrishna/Arank.svg)](https://stars.medv.io/CoderXKrishna/Arank)
----

# Deploy
- [Heroku](#deploy-to-heroku)
- [Okteto](#deploy-to-okteto)
- [Local Machine](#deploy-locally)

# Documentation 
[![Documentation](https://img.shields.io/badge/Documentation-Arank-blue)](http://Arank.tech/)



## Deploy to Heroku
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!  

<p align="center"><a href="https://dashboard.heroku.com/new?template=https://github.com/CoderXKrishna/Arank"> <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-darkred?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

## Deploy to Okteto
Get the [Necessary Variables](#Necessary-Variables) and then click the button below!

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/CoderXKrishna/Arank)

## Deploy Locally
- [Traditional Method](#local-deploy---traditional-method)
- [Easy Method](#local-deploy---easy-method)
- [Arank CLI](#Arank-cli)

### Local Deploy - Easy Method
- Linux - `wget -O locals.py https://git.io/JY9UM && python3 locals.py`
- Windows - `cd desktop ; wget https://git.io/JY9UM -o locals.py ; python locals.py`
- Termux - `wget -O install-termux https://tiny.Arank.tech/termux && bash install-termux`

### Local Deploy - Traditional Method
- Get your [Necessary Variables](#Necessary-Variables)
- Clone the repository:    
`git clone https://github.com/CoderXKrishna/Arank.git`
- Go to the cloned folder:    
`cd Arank`
- Create a virtual env:      
`virtualenv -p /usr/bin/python3 venv`
`. ./venv/bin/activate`
- Install the requirements:      
`pip(3) install -U -r re*/st*/optional-requirements.txt`
`pip(3) install -U -r requirements.txt`
- Generate your `SESSION`:
  - For Linux users:
    `bash sessiongen`
     or
    `wget -O session.py https://git.io/JY9JI && python3 session.py`
  - For Termux users:
    `wget -O session.py https://git.io/JY9JI && python session.py`
  - For Windows Users:
    `cd desktop ; wget https://git.io/JY9JI -o Arank.py ; python Arank.py`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/CoderXKrishna/Arank/blob/main/.env.sample).
(You can either edit and rename the file or make a new file named `.env`.)
- Run the bot:
  - Linux Users:
   `bash startup`
  - Windows Users:
    `python(3) -m pyArank`

---
## Necessary Variables
- `SESSION` - SessionString for your accounts login session. Get it from [here](#Session-String)

One of the following database:
- For **Redis** (tutorial [here](./resources/extras/redistut.md))
  - `REDIS_URI` - Redis endpoint URL, from [redislabs](http://redislabs.com/).
  - `REDIS_PASSWORD` - Redis endpoint Password, from [redislabs](http://redislabs.com/).
- For **MONGODB**
  - `MONGO_URI` - Get it from [mongodb](https://mongodb.com/atlas).
- For **SQLDB**
  - `DATABASE_URL`- Get it from [elephantsql](https://elephantsql.com).

## Session String
Different ways to get your `SESSION`:
* Linux : `wget -O session.py https://git.io/JY9JI && python3 session.py`
* PowerShell : `cd desktop ; wget https://git.io/JY9JI ; python Arank.py`
* Termux : `wget -O session.py https://git.io/JY9JI && python session.py`
* TelegramBot : [@Kanishka_String_Bot](https://t.me/Kanishka_String_Bot)

---

# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
Arank is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

---

# Credits
* [![CoderXKrishna-Devs](https://img.shields.io/static/v1?label=CoderXKrishna&message=devs&color=critical)](https://t.me/ArankDevs)

> Made with 💕 by [@CoderXKrishna](https://t.me/CoderXKrishna).    
