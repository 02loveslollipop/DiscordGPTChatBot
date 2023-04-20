import discord
class ChatRequest:

    def __init__(self,message: str,tts: bool,discordMessage: discord.Message):
        self.tts = tts
        self.message = message
        self.discordMessage = discordMessage
        self.response = ""
        
    
        