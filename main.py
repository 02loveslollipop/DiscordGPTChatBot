import discord
import random
from chatBot import ChatBot
from console import Console
from queueThread import QueueThread
from confLoader import ConfLoader
import asyncio

if __name__ == "__main__":
  config = ConfLoader()
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)
  chatBot = ChatBot(secret=config.open_ai_token,model=config.model,role=config.role,temperature=config.temperature)
  loop = asyncio.get_event_loop()
  checkQueue = QueueThread(chatBot=chatBot,config=config,client=client,timeOutMS=config.timeout)
  checkQueue.run()

@client.event
async def on_ready():
  if config.use_status:
    try:
      await client.change_presence(activity=config.status)
      print(Console.info(f"Status \"{str(config.status)}\" set succesfuly"))
    except:
      print(Console.warning("An error occurr when setting the status, please check config.yml"))

  print(Console.info(f'{config.name} has join with tag {client.user}'))

@client.event

async def on_message(message: discord.Message):
  if message.author == client.user:
    return

  if message.content.startswith(config.s_prefix+'.') and config.b_s_prefix:
    msg = message.content[config.l_s_prefix:]
  elif message.content.startswith(config.prefix+'.'):
    msg = message.content[config.l_prefix:]
  else:
    return
  
  if msg.startswith('.' + config.hello):
    await message.channel.send(config.hello_answer)
  
  if msg.startswith('.' + config.hhelp):
    await message.channel.send(config.help_answer)

  if msg.startswith('.' + config.copypasta) and config.n_copypasta > 0:
    await message.channel.send(config.t_copypasta[random.randint(0,config.n_copypasta-1)])
    
  if msg.startswith('.' + config.version):
    await message.channel.send(config.version_answer)

  if msg.startswith('.' + config.ask + '.' + config.ask_tts + ' ') and config.b_ask_tts == True:
    msg = msg[config.l_ask+config.l_ask_tts+2:]
    await message.channel.send(chatBot.ask(msg), tts=True)
  
  if msg.startswith('.' + config.ask + '.' + config.ask_voice + ' ') and config.b_use_audio == True:
    msg = msg[config.l_ask+config.l_ask_voice+2:]
    chatBot.ask(message=msg,tts=True,discordMessage=message)
  
  if msg.startswith('.' + config.ask + ' '):
    msg = msg[config.l_ask+2:]
    chatBot.ask(message=msg,discordMessage=message,tts=False)
  
  if msg.startswith('.' + config.reset):
    if(chatBot.reset()):
      await message.channel.send(config.reset_error)
    else:
      await message.channel.send(config.reset_success)
  
  if msg.startswith('.' + config.change_role + ' '):
    #msg = message.content
    msg = msg[config.l_change_role+2:]
    chatBot.change_role(msg)
    await message.channel.send(config.role_changed + msg)
        
  if msg.startswith('.' + config.join) and config.b_use_audio:
    if (message.author.voice): 
      channel = message.author.voice.channel
      await channel.connect()
      
      await message.channel.send(config.join_success)
    else: 
        await message.channel.send(config.join_error)
  elif config.b_use_audio == False:
    print(Console.warning("You aren't using audio_related commands, set use_audio: True in config.yml to use it"))
  
  if msg.startswith('.' + config.leave) and config.b_use_audio:
    if (message.guild.voice_client):
      await message.guild.voice_client.disconnect()
      await message.channel.send(config.leave_success)
    else:
      await message.channel.send(config.join_error)
  elif not config.b_use_audio:
    print(Console.warning("You aren't using audio_related commands, set use_audio: True in config.yml to use it"))

client.run(config.bot_token)