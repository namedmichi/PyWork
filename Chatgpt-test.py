import openai 

schnittstelle = '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'

def befehl(details):
  anfrage = openai.Completion.create(model="text-davinci-003", prompt=details, max_tokens=1024, api_key=schnittstelle)
  nachricht = anfrage.choices[0].text
  return nachricht

ergebnis = befehl('Erstelle eine Webseite mit Header, Footer und mehreren Kacheln im Flexbox-Layout.')
print(ergebnis)