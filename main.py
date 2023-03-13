import os
import discord
from frijolito import Bean
from gtts import gTTS as tts
version = "0.03 aplha" # Version actual del Bot
#Comprobacion de en que sistema se esta ejecutando
if os.name == 'nt':
  my_secret = str(Bean.token)
else:
  my_secret = os.environ['TOKEN']
  
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#variables globales
#si frijolito esta en un canal de voz o no

@client.event
async def on_ready():
  print(f'Frijolito se unio con el tag {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('frijolito.hello'):
    await message.channel.send(
      'Hola!, soy frijolito, el mejor NPC de la UPB, ahora implementado en Discord, espero ayudarte en tu dia a dia'
    )

  if message.content.startswith('frijolito.copypasta'):
    await message.channel.send(
      "Albion Online es un mmorpg no lineal, en el que escribes tu propia historia sin limitarte a seguir un camino prefijado. Explora un amplio mundo abierto con 5 biomas únicos, todo cuánto hagas tendrá su repercusión en el mundo, con la economía orientada al jugador de Albion, los jugadores crean prácticamente todo el equipo a partir de los recursos que consiguen, el equipo que llevas define quién eres, cambia de arma y armadura para pasar de caballero a mago, o juega como una mezcla de ambas clases. Aventúrate en el mundo abierto frente a los habitantes y las criaturas de Albion, inicia expediciones o adéntrate en mazmorras en las que encontrarás enemigos aún más difíciles, enfréntate a otros jugadores en encuentros en el mundo abierto, lucha por los territorios o por ciudades enteras en batallas tácticas, relájate en tu isla privada, donde podrás construir un hogar, cultivar cosechas y criar animales, únete a un gremio, todo es mejor cuando se trabaja en grupo. Adéntrate ya en el mundo de Albion y escribe tu propia historia."
    )
    
  if message.content.startswith('frijolito.version'):
    await message.channel.send('Aqui frijolito, mi version actual es: ' + version)
    
  if message.content.startswith('frijolito.join'):
    if (message.author.voice): # Si la persona esta en el canal
        channel = message.author.voice.channel
        vc = await channel.connect()
        await message.channel.send('Me he unido al canal de voz')
        beanify = True
        print("frijolito se ha unido")
    else: # Pero si no esta en un canal de voz
        await message.channel.send("Soy frijolito, pero tu lo eres mas,debes estar primero en un canal de voz para poder unirme a el")

  
  if message.content.startswith('frijolito.leave'):
    if (message.guild.voice_client): # Si el bot se encuentra en un canal de voz
      await message.guild.voice_client.disconnect() # Hace que salga del canal
      await message.channel.send('He salido satisfactoriamente del canal de voz')
      beanify = False
    else: # si no esta en un canal de voz
      await message.channel.send("Soy frijolito, pero tu lo eres mas, no estoy en un canal de voz por lo que no puedo salir")
  
  if message.content.startswith('frijolito.say '):
    if message.guild.voice_client:
      msg = message.content
      msg = msg[14:]
      sound = tts(text=msg,lang="es", slow=False)
      sound.save("tts.mp3")
      source = await discord.FFmpegOpusAudio.from_probe("tts.mp3", method="fallback")
      vc.play(source)
    else:
      await message.channel.send("Soy frijolito, pero tu lo eres mas, debo estar en un canal de voz para hablar")
    
    
    
    

      

    
    


client.run(my_secret)
