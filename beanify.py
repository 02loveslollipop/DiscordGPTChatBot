import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
print(os.getenv("AI_TOKEN"))

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "tu eres un estudiante que es un frijolito, no sabe nada"},
            {"role": "user", "content": "que es la derivacion logaritmica"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)