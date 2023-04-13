# la idea es que cada vez que se genera un comando tipo ask se genere un chatRequest, el cual se encontrara en una lista, habra una rutina la cual se encarga de ir solucionando cada uno de los chat request a medida que estos se generan, asi se pueden hacer varias preguntas a la vez

class ChatRequest:

    def __init__(self,message: str,tts: bool,discordMessage):
        self.tts = tts
        self.message = message
        self.discordMessage = discordMessage
        self.response = ""
        
    
        