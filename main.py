import os
import discord
version = "0.01 aplha"
#Desactivar esta linea al usar en replit
#my_secret = os.environ['TOKEN']
#Desactivar esta linea en visual


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'Hola frijolito esta listo como {client.user}')


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
    await message.channel.send(version)


client.run(my_secret)
