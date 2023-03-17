# xX_frijolito23_Xx
## ATENTION: This repo is probably outdated in the Discord and OpenAI API at some point, so please check for the compatibility
This is just a demo for a personalize role chatbot for Discord using OpenAI API.
#
## Overview
This Python repo implement a chat bot for discord, but it allows to change it role, this will change the way how the GPT model answers the questions, this can even allow it to don't answer a question, or to characterize a certain "personality".

## Requirements

1. You must a have a valid OpenAI API key to use it services (The model used is **GPT-3.5-turbo**).
2. You need a valid Discord bot Token.
3. a Python environment to run the repo.
# Setup
## 1. Discord and OpenAI setup

1. You need a Discord account, then you have to access to the [Discord Developer Portal](https://discord.com/developers/applications)

2. Then you will need to create a new application, you must give it a name, but you can change the name later

3. Now in the **Bot** menu you will click **Add Bot**, there you can select an icon for the bot or change it username, after this you will click **View Token**, this token its your secret token to get access via the API, **you must save this Token and you shouldn't share it publicly**

4. Then in the **OAuth2** submenu you must search for the **URL Generator** submenu, there you will need the permissions required for you app, the you will need to check **"bot"** and **"applications.commands"**, then when you check those option you will get a new window called **"BOT PERMISSIONS"**, in this windows you have to check the permissions, if you are going to edit the code of the bot and add other features you must check which permissions would be required and check it at this point, the minimum permissions are:
    - Read Messages/View Channels
    - Send Messages
    - Send TTS Messages
    - Embed Links
    - Attach Files

5. After checking the permissions you will have a discord link, this discord will allow you to associate your discord bot with your discord server, paste that link into your browser and add your bot into the server where you are going to test it

6. Now it's time to create an OpenAI API Key, to do this you should have an OpenAI Developer Account, then in the [View API Keys](https://platform.openai.com/account/api-keys) you can create a new secret key, **you must save this secret key and you shouldn't share it publicly**

## 2. Python script setup method 1 (Replit)

1. Create a new replit and clone this repository or fork this [Replit](https://replit.com/@02loveslollipop/Frijolito23)

2. Then in the **Tools** menu go to **Secrets**, there you create 2 new enviroment variable:
    - OPEN_AI: The value will be the OpenAI secret key

    - TOKEN: The value will be the Discord Bot token

4. Now in the [Main.py](https://github.com/02loveslollipop/xXfrijolito23Xx/blob/main/main.py) file you should change the variable **call_sign** this will be the preffix for all the commands of the bot

5. Now press **Run**, the first time the replit execute the  poetry package manager will install the required libraries so it will take a while

6. Now check in your Discord server using the command

``
call_sign.hello
``
## 2. Python script setup method 2 (Local Windows)
1. 

## 3. AWS setup (Method 2) **ADVANCE**:

1. 

