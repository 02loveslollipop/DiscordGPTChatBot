class ChatRequest:

    def __init__(self,message: str,tts: bool,discordMessage):
        self.tts = tts
        self.message = message
        self.discordMessage = discordMessage
        self.response = ""
        
    
        