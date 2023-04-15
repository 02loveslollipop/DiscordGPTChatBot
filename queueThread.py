from chatBot import ChatBot
from chatRequest import ChatRequest
from confLoader import ConfLoader
import discord
import asyncio
import time
from threading import Thread
from console import Console

class QueueThread:
    def __init__(self,chatBot: ChatBot,config: ConfLoader):
        self.chatBot = chatBot
        self.config = config
        self.loop = asyncio.get_event_loop()
     
    def checkQueue(self):
        while True:
            if self.chatBot.n_request > 0:
                chatRequest = self.chatBot.sendChatCompletition()
                if chatRequest.tts:
                    if (chatRequest.discordMessage.guild.voice_client):
                        self.config.tts.synth(message=chatRequest.response)
                        source = self.convertAudioStream()
                        chatRequest.discordMessage.guild.voice_client.play(source)
                    else:
                        task = asyncio.create_task(self.sendDiscordMessage(chatRequest=chatRequest,message=self.config.leave_error))
                        self.loop.run_until_complete(task)     
                else:
                    task = asyncio.create_task(self.sendDiscordMessage(chatRequest=chatRequest,message=chatRequest.response))
                    self.loop.run_until_complete(task)
                    

            
 
            #time.sleep(1)
    
    async def convertAudioStream():
        try:
            return await discord.FFmpegOpusAudio.from_probe("tts.wav", method="fallback")
        except:
            return None
    
    async def sendDiscordMessage(self,chatRequest: ChatRequest,message: str):
        try:
            await chatRequest.discordMessage.channel.send(message)
            return True
        except:
            return False 
        
        
    
    def start(self):
            process = Thread(target=self.checkQueue)
            process.start()
            print(Console.info("ChatCompletitionThread initialized succesfuly"))
        