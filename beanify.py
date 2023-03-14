import os
from flask import Flask, redirect, render_template, request, url_for
from frijolito import BeanGPT

#openai.api_key = os.getenv("OPENAI_API_KEY")


class Beanify:
    import openai
    
    def __init__(self):
        self.nbeanify = 0
        if os.name == 'nt':
            my_secret = str(BeanGPT.token)
        else:
            my_secret = os.environ['OPEN_AI']
        self.openai.api_key = my_secret
        
        self.id_bot = "eres una persona con una capacidad intelectual igual a la de un niño de 5 años, te llamas Frijolito, estudias ingenieria en entretenimiento digital en la UPB, tengo sindrome dawn y me gusta jugar minecraft con mis amigos ratas todo el dia"
        
        self.prompt=[
                    {"role": "system", "content": self.id_bot}
                ]
        
    
    def ask_frijolito(self,message):
        self.prompt.append({"role": "user", "content": message})
        response = self.openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.prompt
        )
        self.nbeanify=self.nbeanify+1
        result = ''
        for choice in response.choices:
            result += choice.message.content

        self.prompt.append({"role": "assistant", "content": result})
        return result
    
    def reset_frijolito(self):
        if(self.nbeanify == 0):
            return True
        else:
            self.prompt=[{"role": "system", "content": self.id_bot}]
            self.nbeanify == 0
            return False
    
    def change_frijolito_identity(self,identity):
        self.prompt[0] = {"role": "system", "content": identity}

