class ChatBot:
    
    import openai
    
    def __init__(self,secret,model,role):
        self.openai.api_key = secret
        self.role = role
        self.model = model
        self.prompt=[
                    {"role": "system", "content": self.role}
                ]
        self.n_request = 0
        
    
    def ask(self,message):
        self.prompt.append({"role": "user", "content": message})
        response = self.openai.ChatCompletion.create(
            model=self.model,
            messages=self.prompt
        )
        self.n_request+=1
        result = ''
        for choice in response.choices:
            result += choice.message.content

        self.prompt.append({"role": "assistant", "content": result})
        return result
    
    def reset(self):
        if(self.n_request == 0):
            return True
        else:
            self.prompt=[{"role": "system", "content": self.role}]
            self.n_request == 0
            return False
    
    def change_role(self,role):
        if(self.n_request == 0):
            return True
        else:
            self.prompt=[{"role": "system", "content": role}]
            self.n_request == 0
            return False

