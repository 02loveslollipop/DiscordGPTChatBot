import discord
import random
import yaml
from chatBot import ChatBot
from console import Console
from text2speech import GoogleCloudTTS
from text2speech import Gtts
import traceback

vc = None

try:
  config_file = open('config.yml')
  print(Console.info("Using config.yml"))
  
except FileNotFoundError:
  print(Console.warning("You don't have a config.yml file, using example_config.yml"))
  config_file = open('example_config.yml')

finally:
  try:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
    prefix = config['bot']['prefix']
    name = config['bot']['name']
    bot_token = config['bot']['token']
    b_ask_tts = config['bot']['use_ask_tts']
    
    if config['bot']['use_short_prefix']:
      s_prefix = config['bot']['short_prefix']
      b_s_prefix = True
    else: 
      b_s_prefix = False
      s_prefix = ''

    if config['bot']['use_copypasta']:
      t_copypasta = config['text']['copypasta']
      n_copypasta = len(t_copypasta)
    else: n_copypasta = 0
    
    if config['bot']['use_audio']:
      join = config['command']['join']
      leave = config['command']['leave']
      ask_voice = config['command']['ask_voice']
      join_error = config['text']['join_error']
      join_success = config['text']['join_success']
      leave_success = config['text']['leave_success']
      leave_error = config['text']['leave_error']
      b_use_audio = True
      if config['TTS']['engine'] == "gcloud":
        tts = GoogleCloudTTS(config['TTS']['model'])
      elif config['TTS']['engine'] == "gtts":
        tts = Gtts(config['TTS']['language'],config['TTS']['tld'])
    else:
      b_use_audio = False
      join = None
      leave = None
      
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
    if config['status']['use_status']:
      use_status = True
      if config['status']['use_help_command'] and "{help_command}" in config['status']['text']:
        text = config['status']['text']
        text = text.format(help_command=(prefix + '.' + hhelp))
      else:
        text = config['status']['text']
      if config['status']['status_type'] == 'game':
        status = discord.Game(name=text)
      elif config['status']['status_type'] == 'streaming':
        url = config['status']['streaming_url']
        status = discord.Streaming(name=text,url=url)
      elif config['status']['status_type'] == 'listening':
        status = discord.Activity(type=discord.ActivityType.listening, name=(text))
      elif config['status']['status_type'] == 'watching':
        status = discord.Activity(type=discord.ActivityType.watching, name=text)
      else:
        print(Console.warning("Status configuration isn't right please check it, status will be disable"))
        use_status = False
    else: use_status = False
  
  except KeyError as err:
    print(Console.error(str(type(err))))
    print(Console.error(str(err.args)))
    print(Console.error(str(traceback.format_exc())))
    print(Console.warning("The bot couldn't start because of a bad configuration in confg.yml, please check your confg.yml"))
    exit()

l_prefix = len(prefix)
l_s_prefix = len(s_prefix)
l_helo = len(hello)
l_copypasta = len(copypasta)
l_version = len(version)
l_ask = len(ask)
l_ask_tts = len(ask_tts)
l_reset = len(reset)
l_change_role = len(change_role)
l_join = len(join)
l_leave = len(leave)
l_ask_voice = len(ask_voice)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
chatBot = ChatBot(secret=open_ai_token,model=model,role=role)

@client.event
async def on_ready():
  if use_status:
    try:
      await client.change_presence(activity=status)
      print(Console.info(f"Status \"{str(status)}\" set succesfuly"))
    except:
      print(Console.warning("An error occurr when setting the status, please check config.yml"))

  print(Console.info(f'{name} has join with tag {client.user}'))

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
    msg = msg[l_ask+l_ask_tts+2:]
    await message.channel.send(chatBot.ask(msg), tts=True)
  
  if msg.startswith('.' + ask + '.' + ask_voice + ' ') and b_use_audio == True: #TODO: aca estoy trabajando
    if (message.guild.voice_client):
      msg = msg[l_ask+l_ask_voice+2:]
      tts.synth(message=chatBot.ask(msg))
      source = await discord.FFmpegOpusAudio.from_probe("tts.wav", method="fallback")
      message.guild.voice_client.play(source)
    else:
      await message.channel.send(leave_error)
  
  if msg.startswith('.' + ask + ' '):
    msg = msg[l_ask+2:]
    await message.channel.send(chatBot.ask(msg))
  
  if msg.startswith('.' + reset):
    if(chatBot.reset()):
      await message.channel.send(reset_error)
    else:
      await message.channel.send(reset_success)
  
  if msg.startswith('.' + change_role + ' '):
    #msg = message.content
    msg = msg[l_change_role+2:]
    chatBot.change_role(msg)
    await message.channel.send(role_changed + msg)
        
  if msg.startswith('.' + join) and b_use_audio:
    if (message.author.voice): 
      channel = message.author.voice.channel
      vc = await channel.connect()
      await message.channel.send(join_success)
    else: 
        await message.channel.send(join_error)
  elif b_use_audio == False:
    print(Console.warning("You aren't using audio_related commands, set use_audio: True in config.yml to use it"+"ERROR EN 1"))
  
  if msg.startswith('.' + leave) and b_use_audio:
    if (message.guild.voice_client):
      await message.guild.voice_client.disconnect()
      await message.channel.send('He salido satisfactoriamente del canal de voz')
    else:
      await message.channel.send("Soy frijolito, pero tu lo eres mas, no estoy en un canal de voz por lo que no puedo salir")
  elif b_use_audio == False:
    print(Console.warning("You aren't using audio_related commands, set use_audio: True in config.yml to use it"))

client.run(bot_token)