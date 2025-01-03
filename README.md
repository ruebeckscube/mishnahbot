# ![](logo_small.png) Mishnabot 

Mishnabot is a Discord bot that posts a random mishnah sugye once per day (except on Shabbos). The bilingual Mishnah text was scraped from [Sefaria](https://www.sefaria.org/texts).

# Covenant

This software uses the MIT license, which you can read [here](LICENSE).

This software was originally made for [Shel Maala](https://www.shelmaala.com/) in order to enable the creation of the Queer Talmud. Alternative use cases, such as the study of the non-queer Talmud, are theoretically possible but not actively supported by the developers. Usage of this software to suppress the Queer Talmud is prohibited.

The user of this software may not be an individual or entity, or a representative, agent, affiliate, successor, attorney, or assign of an individual or entity, identified by the Boycott, Divestment, Sanctions ("BDS") movement on its website ([https://bdsmovement.net/](https://bdsmovement.net/) and [https://bdsmovement.net/get-involved/what-to-boycott](https://bdsmovement.net/get-involved/what-to-boycott)) as a target for boycott. *[Source: The Hippocratic License](https://firstdonoharm.dev/#hippocratic-license-3-0)*

# Requirements

- A remote server
- On your computer, git and Python 3.6 or newer
- On the server, Python 3.6 or newer
- Admin privileges on the target Discord server

# Setup 

## 1. Discord

1. [Create a Discord bot.](https://gizmodo.com/how-to-make-a-discord-bot-1847378375)
2. [Get the ID of the channel you want the bot to post to.](https://docs.statbot.net/docs/faq/general/how-find-id/)
3. Get the OAuth2 client ID of the bot (you'll need this in order to add it to the channel).
4. [Add the bot to the channel.](https://discord.com/oauth2/authorize?client_id=945422849622032395&scope=bot&permissions=0) (Replace the client ID with your bot's client ID)

## 2. Your remote server

1. Get Python running on your server. How to do this will vary depending on the webhost.
2. Make sure you can ftp and ssh into the server.

## 3. Your local computer

1. Clone this repo. The rest of this documentation assumes that you've cloned the repo to `~/mishnabot` where `~` is your home directory.
2. Create a file named `secrets.txt` in the same directory as this file, formatted like this:

```
ssh_username=USERNAME
ssh_password=PASSWORD
ftp_username=USERNAME
ftp_password=PASSWORD
ftp=ftp.URL
hostname=URL
ssh_cwd=URL/PATH
```

- `USERNAME` and `PASSWORD` are your login credentials.
- `URL` is the server url, for example `my_server.com`
- `URL/PATH` is the path to the directory where the Discord bot should be uploaded. The `.htaccess` file will be uploaded here and everything else will be uploaded to `URL/PATH/public/`.

3. Create a file named `bot_secrets.txt` in the same directory as this file, formatted like this:

```
token=BOT_TOKEN
mishnah_channel=CHANNEL_ID
mussar_channel=CHANNEL_ID
mussar_start=ISO_DATE
```

`mussar_start` is the date in ISO format (`YYYY-MM-DD`, e.g. `2024-01-30`) on
which you'd like to start the daily mussar prompts. Leave out the mussar
information to disable daily mussar prompts.

In a terminal:

1. `cd ~/mishnabot`
2. `python3 ftp.py` This will upload mishnabot to your server. On Windows, run `py -3 ftp.py` instead.
3. `ssh USERNAME@SERVER` 
4. `cd path/to/mishnabot`
5. `python3 -m pip install -e .`
6. `timedatectl` to get the timezone of your server.
7. `crontab -e`
8. Add this line to the crontab file:

```
0 15 * * 0-5 python3 ~/PATH/run.py > ~/path/to/log.txt
```

Replace `15` (3:00 PM) with the correct time.

Replace `PATH` with the actual path on the server, for example `~/my_server.com/public/run.py`

9. To exit nano, `ctrl+x` and `y` and `enter`
10. `exit`

# Changelog

## 1.1.0

- Removed `launch.py`
- Removed `get_log.py`
- Removed `get_process.py`
- Removed `ssh.py`
- Removed `spur` requirement
- Refactored most of `run.py` so that it works via crontab

## 1.0.2

- Fixed: `run.py` args `--shomer` and `--logging` aren't actually used.
- Added arg `--shabbos` to `run.py` and `Bot` to set which day is Shabbos.

## 1.0.1

Minor changes

## 1.0.0

- Added parameter `shomer` to `Bot` and `run.py`. If True, don't post on Shabbos
- Added parameter `logging` to `Bot` and `run.py` If True, log messages
  - Added logging to `Bot`
- Moved ssh code to `mishnabot.ssh.py`
  - Added `get_log.py` and `get_process.py` to check on the bot's status
- Renamed `ssh.py` to `launch.py`
- Explicitly set which files get uploaded via `ftp.py`
