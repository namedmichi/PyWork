# Code in einem Block
import openai 

schnittstelle = ''

def befehl(details):
  anfrage = openai.Completion.create(model="text-davinci-003", prompt=details, max_tokens=64, api_key=schnittstelle)
  nachricht = anfrage.choices[0].text
  return nachricht

ergebnis = befehl('How can i center a div')
print(ergebnis)