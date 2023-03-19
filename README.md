# Discord GPT Chat Bot

> Python script This is just a demo for a personalize role chatbot for Discord using OpenAI API.

## Intro
OpenAI GPT3.5 model allow to change it behavior using custom training and using system role messages, this repository allows to create a Discord Bot using the GPT 3.5 model with a custom role allowing to change the behavior of the answers of the bot.

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

2. Create a copy of ``example_config.yml`` and rename it as ``config.yml`` open it and configure the bot **(A full guide of the config file can be found [here](TODO: add link))**:

```yaml
bot:
  token: "YOUR_DISCORD_KEY" # Paste here the token you got from Discord Developer Portal

open_ai:
  token: "YOUR_OPEN_AI_KEY" # Paste here the OpenAI secret key you got from OpenAI platform
  role: "You are a helpful assistant." # Change here chatbot's role, this will change it's behavior answering questions
```

3. Now press **Run**, the first time the Replit execute the  poetry package manager will install the required libraries so it will take a while

4. Now check in your Discord server using the command

```discord
your_prefix.hello
```

## 2. Python Script setup - Method 2 (Local Windows)
1. Install ``Python 3.9.16`` using the [Python page](https://www.python.org/downloads/release/python-3916/)

2. Clone the repository, you can either download the repository as a [.zip](https://github.com/02loveslollipop/xXfrijolito23Xx/archive/refs/heads/main.zip) and unzip, or clone the repository using git:
```powershell
git clone https://github.com/02loveslollipop/xXfrijolito23Xx.git
```

3. Create a copy of ``example_config.yml`` and rename it as ``config.yml`` open it and configure the bot **(A full guide of the config file can be found [here](TODO: add link))**:

```yaml
bot:
  token: "YOUR_DISCORD_KEY" # Paste here the token you got from Discord Developer Portal

open_ai:
  token: "YOUR_OPEN_AI_KEY" # Paste here the OpenAI secret key you got from OpenAI platform
  role: "You are a helpful assistant." # Change here chatbot's role, this will change it's behavior answering questions
```

4. Now in the root of the repository execute this command to update all the required libraries:

```powershell
pip -r requirements.txt
```

5. Then execute the python script in the root of the repository:

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

```bash
ssh -i "identityfile.pem" ubuntu@your_public_dns.compute-1.amazonaws.com
```

6. Install Python 3.9 in the EC2 instance, as this isn't the last release we are going to get it from the deadsnakes PPA:
```bash
sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa 
sudo apt install python3.9 -y
sudo apt install python3-pip -y
```
7. Then we are going to check if we installed the correct version, it should say ``Python 3.9.xx``

8. Clone the repository:

```bash
git clone https://github.com/02loveslollipop/xXfrijolito23Xx.git
```

9. Create a copy of ``example_config.yml`` and rename it as ``config.yml``:

```bash
cp example_config.yml config.yml
```

10. Open ``config.yml`` and configure the bot **(A full guide of the config file can be found [here](TODO: add link))**:

```yaml
bot:
  token: "YOUR_DISCORD_KEY" # Paste here the token you got from Discord Developer Portal

open_ai:
  token: "YOUR_OPEN_AI_KEY" # Paste here the OpenAI secret key you got from OpenAI platform
  role: "You are a helpful assistant." # Change here chatbot's role, this will change it's behavior answering questions
```

11. Now execute this command to update all the required libraries:

```bash
pip -r /path/to/your/repo/requirements.txt
```

12. After that let's create a service so every time the system reboot it starts again the script:

```bash
sudo nano /etc/systemd/system/discord_bot.service
```

13. In the file write this script, and then save it:

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

14. Reload the Systemd daemon to recognize the new service:

```console
sudo systemctl enable my-script.service
```

15. Enable the service:

```console
sudo systemctl enable discord_bot.service
```

16. Start the service:

```bash
sudo systemctl start dicord_bot.service
```

17. Now check in your Discord server using the command

```discord
your_call_sign.hello
```

## Discord Commands
[Full list of commands here](TODO: add link)

## Configuration of config.yml
[Config.yml configuration guide](TODO: add link)
