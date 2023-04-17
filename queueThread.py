from chatBot import ChatBot
from chatRequest import ChatRequest
from confLoader import ConfLoader
import discord
import asyncio
import time
from threading import Thread
from console import Console

class QueueThread:
    def __init__(self,chatBot: ChatBot,config: ConfLoader,mainLoop):
        self.chatBot = chatBot
        self.config = config
        self.loop = asyncio.get_event_loop()
        self.mainLoop = mainLoop
     
    def checkQueue(self):
        while True:
            if self.chatBot.n_request > 0:
                self.chatRequest = self.chatBot.sendChatCompletition()
                if self.chatRequest.tts:
                    if (self.chatRequest.discordMessage.guild.voice_client):
                        self.config.tts.synth(message=self.chatRequest.response)
                        #source = self.convertAudioStream()
                        task = self.loop.create_task(discord.FFmpegOpusAudio.from_probe("tts.wav"))
                        source = self.loop.run_until_complete(task)
                        self.chatRequest.discordMessage.guild.voice_client.play(source)
                        
                    else:
                        print("trying to send response")
                        mainLooptask = self.mainLoop.create_task(self.chatRequest.discordMessage.channel.send())
                        source = self.mainLoop.run_until_complete(mainLooptask)
                        
                else:
                    print("trying to send response")
                    mainLooptask = self.mainLoop.create_task(self.chatRequest.discordMessage.channel.send(self.chatRequest.response))
                    source = self.mainLoop.run_until_complete(mainLooptask)
            time.sleep(1)
            print("sigo")
    
    
        
    async def sendDiscordMessage(self,message,chatRequest):
        await chatRequest.discordMessage.channel.send(message)




    def start(self):
            process = Thread(target=self.checkQueue)
            process.start()
            print(Console.info("ChatCompletitionThread initialized succesfuly"))
        