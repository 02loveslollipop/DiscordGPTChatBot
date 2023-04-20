# Discord GPT Chat Bot

> A Python based Discord chat bot that uses the OpenAI GPT API with a custom role

## Intro
OpenAI GPT3.5 model allow to change it behavior using custom training and using system role messages, this repository allows to create a Discord Bot using the GPT 3.5 model with a custom role allowing to change the behavior of the answers of the bot.

## Requirements

1. You must a have a valid OpenAI API key to use it services (Currently using **GPT-3.5-turbo**).
2. You need a valid Discord bot Token.
3. A Python environment to run the repo.
4. If you want to use voice related commands you need FFmpeg on the device that will run the bot

# Quick Setup

Full setup guide available at [Setup guide](https://github.com/02loveslollipop/DiscordGPTChatBot/wiki/Setup-guide)

1. Install Python 3.9 in your device.

2. Clone the repository: 

```bash
git clone https://github.com/02loveslollipop/DiscordGPTChatBot.git
```

3. Install FFmpeg on your device, FFmpeg can be install [here](https://ffmpeg.org/)


4. Create a copy of ``example_config.yml`` and rename it as ``config.yml``, then open it and paste your Discord and OpenAI keys and change the role of the chat bot (Full description of [config.yml](https://github.com/02loveslollipop/DiscordGPTChatBot/wiki/Structure-of-config.yml)):

```yaml
bot:
  token: "YOUR_DISCORD_KEY" # Paste here the token you got from Discord Developer Portal

open_ai:
  token: "YOUR_OPEN_AI_KEY" # Paste here the OpenAI secret key you got from OpenAI platform
  role: "You are a helpful assistant." # Change here chatbot's role, this will change it's behavior answering questions
```

5. Install requirements:

```bash
pip -r /path/to/your/repo/requirements.txt
```

6. Run the bot:

```bash
python main.py
```


# Discord Commands
[Full list of commands here](https://github.com/02loveslollipop/DiscordGPTChatBot/wiki/Discord-commands)

# Configuration of config.yml
[Config.yml configuration guide](https://github.com/02loveslollipop/DiscordGPTChatBot/wiki/Structure-of-config.yml)
