import os
import discord
import random
import yaml
from chatBot import ChatBot

try:
  config_file = open('config.yml')
  
except FileNotFoundError:
  print("You don't have a config.yml file, using example_config.yml")
  config_file = open('example_config.yml')

finally:
  config = yaml.load(config_file, Loader=yaml.FullLoader)
  prefix = config['bot']['prefix']
  name = config['bot']['name']
  bot_token = config['bot']['token']
  b_ask_tts = config['bot']['use_ask_tts']
  
  if(config['bot']['use_short_prefix']):
    s_prefix = config['bot']['short_prefix']
    b_s_prefix = True
  else: 
    b_s_prefix = False
    s_prefix = ''
    
  if(config['bot']['use_copypasta']):
    t_copypasta = config['text']['copypasta']
    n_copypasta = len(t_copypasta)
  else: n_copypasta = 0
  
  open_ai_token = config['open_ai']['token']
  model = config['open_ai']['model']
  role = config['open_ai']['role']
  help_answer = config['text']['help']
  hello_answer = config['text']['hello']
  version_answer = config['text']['version']
  reset_error = config['text']['reset_error']
  reset_success = config['text']['reset_success']
  role_changed = config['text']['role_changed']
  hhelp = config['command']['help']
  hello = config['command']['hello']
  copypasta = config['command']['copypasta']
  version = config['command']['version']
  ask = config['command']['ask']
  ask_tts = config['command']['ask_tts']
  reset = config['command']['reset']
  change_role = config['command']['change_role']
    
l_prefix = len(prefix)
l_s_prefix = len(s_prefix)
    
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
chatBot = ChatBot(secret=open_ai_token,model=model,role=role)

@client.event
async def on_ready():
  print(f'{name} has join with tag {client.user}')
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(s_prefix+'.') and b_s_prefix:
    msg = message.content[l_s_prefix:]
  elif message.content.startswith(prefix+'.'):
    msg = message.content[l_prefix:]
  else:
    return
  
  if msg.startswith('.' + hello):
    await message.channel.send(hello_answer)
  
  if msg.startswith('.' + hhelp):
    await message.channel.send(help_answer)

  if msg.startswith('.' + copypasta) and n_copypasta > 0:
    await message.channel.send(t_copypasta[random.randint(0,n_copypasta-1)])
    
  if msg.startswith('.' + version):
    await message.channel.send(version_answer)

  if msg.startswith('.' + ask + '.' + ask_tts + ' ') and b_ask_tts == True:
    msg = msg[9:]
    await message.channel.send(chatBot.ask(msg), tts=True)
  
  if msg.startswith('.' + ask + ' '):
    msg = msg[5:]
    await message.channel.send(chatBot.ask(msg))
  
  if msg.startswith('.' + reset):
    if(chatBot.reset()):
      await message.channel.send(reset_error)
    else:
      await message.channel.send(reset_success)
  
    if message.content.startswith('.' + change_role):
      msg = message.content
      msg = msg[12:]
      chatBot.change_role(msg)
      await message.channel.send(role_changed + msg)
        
client.run(bot_token)