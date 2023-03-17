# Frijolito discord bot
## ATENTION: This repo is probably outdated in the Discord and OpenAI API at some point, so please check for the compatibility
This is just a demo for a personalize role chatbot for Discord using OpenAI API.
#
## Overview
This Python repo implement a chat bot for discord, but it allows to change it role, this will change the way how the GPT model answers the questions, this can even allow it to don't answer a question, or to characterize a certain "personality".

## Requirements

1. You must a have a valid OpenAI API key to use it services (The model used is **GPT-3.5-turbo**).
2. You need a valid Discord bot Token.
3. A Python environment to run the repo.
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

## 2. Python Script setup - Method 1 (Replit)

1. Create a new replit and clone this repository or fork this [Replit](https://replit.com/@02loveslollipop/Frijolito23)

2. Then in the **Tools** menu go to **Secrets**, there you create 2 new enviroment variable:
    - ``OPEN_AI``: The value will be the OpenAI secret key

    - ``TOKEN``: The value will be the Discord Bot token

4. Now in the [Main.py](https://github.com/02loveslollipop/xXfrijolito23Xx/blob/main/main.py) file you should change the variable ``call_sign`` this will be the preffix for all the commands of the bot

5. Now press **Run**, the first time the Replit execute the  poetry package manager will install the required libraries so it will take a while

6. Now check in your Discord server using the command

```discord
your_call_sign.hello
```

## 2. Python Script setup - Method 2 (Local Windows)
1. Install ``Python 3.9.16`` using the [Python page](https://www.python.org/downloads/release/python-3916/)

2. Clone the repository, you can either download the repository as a [.zip](https://github.com/02loveslollipop/xXfrijolito23Xx/archive/refs/heads/main.zip) and unzip, or clone the repository using git:
```powershell
git clone https://github.com/02loveslollipop/xXfrijolito23Xx.git
```

3. Create 2 files in the parent directory where you clone the repository
    - ``token.key``: it contains the Discord bot token
    - ``openai.key``: it contais the OpenAI API key

4. Now in the [Main.py](https://github.com/02loveslollipop/xXfrijolito23Xx/blob/main/main.py) file you should change the variable ``call_sign`` this will be the preffix for all the commands of the bot

5. Now in the root of the repository execute this command to update all the required libraries:

```powershell
pip -r requirements.txt
```

6. Then execute the python script in the root of the repository:

```powershell
python main.py
```

6. Now check in your Discord server using the command

```discord
your_call_sign.hello
```

## 3. Python Script setup - Method 3 **ADVANCE** (Ubuntu - AWS)

1. First you must log in to your AWS console and navigate to the EC2 dashboard

2. After that click on the "Launch Instance" button and select the Ubuntu Server AMI.

3. Now choose the instance type (for this case it doesn't require a lot of resources so an ``t2.micro`` would be enough) and configure the instance details, such as VPC, subnet, and security groups.

4. In the "Add Storage" section, you can configure the size and type of storage (this instance doesn't require a lot of memory or a high speed memory so 8GB of GP2 is enough)
In the "Add Tags" section, you can add any relevant tags to help you organize and track your instances.

5. After the instances is setup access via SSH using the identity file that you use to setup the EC2 instance:

```console
ssh -i "identityfile.pem" ubuntu@your_public_dns.compute-1.amazonaws.com
```

6. Install Python 3.9 in the EC2 instance, as this isn't the last release we are going to get it from the deadsnakes PPA:
```console
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa 
sudo apt install python3.9 -y
sudo apt install python3-pip -y
```
7. Then we are going to check if we installed the correct version, it should say ``Python 3.9.xx``

8. Clone the repository:

```console
git clone https://github.com/02loveslollipop/xXfrijolito23Xx.git
```

9. Now let's add our Discord token and OpenAI API key as environment variables in our server, for that open the .bashrc of the user where we are going to execute the script:

```console
nano ~/.bashrc
```

10. Now add the environment variables, and the save the file:

```bash
export OPEN_AI="your OpenAI secret key"
export TOKEN="your Discord Bot token"
```

11. Then execute the .bashrc file to make the environment variables available:

```console
source ~/.bashrc
```

12. Now in the [Main.py](https://github.com/02loveslollipop/xXfrijolito23Xx/blob/main/main.py) file you should change the variable ``call_sign`` this will be the prefix for all the commands of the bot

13. Now execute this command to update all the required libraries:

```console
pip -r /path/to/your/repo/requirements.txt
```

14. After that let's create a service so every time the system reboot it starts again the script:

```console
sudo nano /etc/systemd/system/discord_bot.service
```

15. In the file write this script, and then save it:

```bash
[Unit]
Description=Discord bot service

[Service]
Type=simple
ExecStart=/usr/bin/python3 /path/to/your/repo/main.py
Restart=always
User=ubuntu

[Install]
WantedBy=multi-user.target
```

16. Reload the Systemd daemon to recognize the new service:

```console
sudo systemctl enable my-script.service
```

17. Enable the service:

```console
sudo systemctl enable discord_bot.service
```

18. Start the service:

```bash
sudo systemctl start dicord_bot.service
```

19. Now check in your Discord server using the command

```discord
your_call_sign.hello
```
