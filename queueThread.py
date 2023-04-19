from chatBot import ChatBot
from chatRequest import ChatRequest
from confLoader import ConfLoader
import discord
import asyncio
import time
from threading import Thread
from console import Console

class QueueThread:
    def __init__(self,chatBot: ChatBot,config: ConfLoader,client: discord.Client):
        milisec = 100
        self.timeout = (1/milisec)
        self.chatBot = chatBot
        self.config = config
        self.loop = asyncio.get_event_loop()
        self.client = client
     
    def checkQueue(self):
        while True:
            if self.chatBot.n_request > 0:
                self.chatRequest = self.chatBot.sendChatCompletition()
                if self.chatRequest.tts:
                    if (self.chatRequest.discordMessage.guild.voice_client):
                        self.config.tts.synth(message=self.chatRequest.response)
                        task = self.loop.create_task(discord.FFmpegOpusAudio.from_probe("tts.wav"))
                        source = self.loop.run_until_complete(task)
                        self.chatRequest.discordMessage.guild.voice_client.play(source)
                        
                    else:
                        asyncio.run_coroutine_threadsafe(self.sendDiscordMessage(self.config.leave_error,self.chatRequest),self.client.loop)
                        
                else:
                    asyncio.run_coroutine_threadsafe(self.sendDiscordMessage(self.chatRequest.response,self.chatRequest),self.client.loop)
            time.sleep(self.timeout)

    async def sendDiscordMessage(self,message: str,chatRequest: ChatRequest):
        await chatRequest.discordMessage.channel.send(message)

    def start(self):
            process = Thread(target=self.checkQueue)
            process.start()
            print(Console.info("ChatCompletitionThread initialized succesfuly"))
        