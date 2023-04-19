from chatRequest import ChatRequest
import openai  
class ChatBot:
    
    

    
    def __init__(self,secret: str,model: str,role: str,temperature: int):
        self.temperature = temperature
        self.openai.api_key = secret
        self.role = role
        self.model = model
        self.prompt=[
                    {"role": "system", "content": self.role}
                ]
        self.n_request = 0
        self.pendingMessage = []
        
    def sendChatCompletition(self):
        CurrentMessage = self.pendingMessage[0]
        self.prompt.append({"role": "user", "content": CurrentMessage.message})
        self.pendingMessage.pop(0)
        response = openai.ChatCompletion.create(
        model=self.model,
        messages=self.prompt#,
        #temperature=self.temperature
        )
        self.n_request -= 1
        result = ''
        for choice in response.choices:
            result += choice.message.content
        self.prompt.append({"role": "assistant", "content": result})
        CurrentMessage.response = result
        return ChatRequest(CurrentMessage)
            


# la idea es que pueda poner varios mensajes, y que el bot pueda analizar todo, lo

    def ask(self,message: str,tts: bool,discordMessage):
        newChatRequest = ChatRequest(message=message,discordMessage=discordMessage,tts=tts)
        self.pendingMessage.append(newChatRequest)
        self.n_request += 1
            
    def reset(self):
        self.prompt=[{"role": "system", "content": self.role}]
        self.pendingMessage = []
        self.n_request == 0
        return False
    
    def change_role(self,role: str):
        self.prompt=[{"role": "system", "content": role}]
        self.pendingMessage = []
        self.n_request == 0