from chatBot import ChatBot
from chatRequest import ChatRequest
from confLoader import ConfLoader
import discord
import asyncio
import time
from threading import Thread
from console import Console

class QueueThread:
    def __init__(self,chatBot: ChatBot,config: ConfLoader,client: discord.Client,timeOutMS: int = 100):
        self.timeout = (1/timeOutMS)
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
                        voiceTask = self.loop.create_task(self.sendDiscordVoice(source=source,chatRequest=self.chatRequest))
                        result = False
                        while not result:
                            result = self.loop.run_until_complete(voiceTask)
                        
                    else:
                        asyncio.run_coroutine_threadsafe(self.sendDiscordMessage(self.config.leave_error,self.chatRequest),self.client.loop)
                        
                else:
                    asyncio.run_coroutine_threadsafe(self.sendDiscordMessage(self.chatRequest.response,self.chatRequest),self.client.loop)
            time.sleep(self.timeout)

    async def sendDiscordMessage(self,message: str,chatRequest: ChatRequest):
        await chatRequest.discordMessage.channel.send(message)

    async def sendDiscordVoice(self,source: discord.FFmpegOpusAudio,chatRequest: ChatRequest):
        try:
            chatRequest.discordMessage.guild.voice_client.play(source)
            while chatRequest.discordMessage.guild.voice_client.is_playing():
                time.sleep(self.timeout)
            else:
                print(Console.info("Voice Output finished successfully"))
                return True
        except Exception as e:
            print(e)
            return False
        
    def run(self):
            process = Thread(target=self.checkQueue)
            process.start()
            print(Console.info("ChatCompletitionThread initialized successfully"))
        