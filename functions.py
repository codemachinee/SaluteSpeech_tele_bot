import requests
from paswords import *
from api_generate import *

url = 'https://smartspeech.sber.ru/rest/v1/speech:recognize'
headers = {
      'Authorization': f'Bearer {key_generate()}',
      'Content-Type': 'audio/ogg;codecs=opus',

    }

with open(f'audio_2023-12-26_22-19-54.ogg', 'rb') as audio_file:
    response = requests.post(url, headers=headers, data=audio_file, verify=False)
    print(response.json())