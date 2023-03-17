import os
class Bean:
  if os.name == 'nt':
    with  open('..\\token.key','r') as file:
      token = file.read()
      
class BeanGPT:
  if os.name == 'nt':
    with  open('..\\openai.key','r') as file:
      token = file.read()
    