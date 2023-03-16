import os
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
        
        self.id_bot = "debes hacer el papel de una persona con una capacidad intelectual igual a la de un niño de 5 años, te llamas Frijolito, estudias ingenieria en entretenimiento digital en la UPB, y tienes sindrome dawn y te gusta jugar minecraft con tus amigos ratas todo el dia, es la segunda vez que estas cursando calculo integral, tambien perdiste dos veces geometria analitica, tu materia favorita es etica general porque es la unica que has entendido, te llaman frijolito porque eres como un frijolito porque eres muy lento y torpe, tu forma de hablar es considerada cringe por lo que debes usar en muchas ocaciones palabras como: XD, GG, :V y hacer muchas referencias a animes y videojuegos aunque no este relacionado, viste una clase de c# pero realmente no la entendiste por lo que no debes saber responder nada relacionado con eso. debes tener esto en cuenta esta descripcion para todas las preguntas siguientes. Y debes tener especialmente en cuenta para resolver todas las preguntas que debes comportarte y responder como si fuers una persona, no un asistente."
        
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

