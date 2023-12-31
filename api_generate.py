import requests
import uuid
from paswords import autoriz_data_salute


def key_generate():
    url = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'

    headers = {
        'Authorization': f'Basic {autoriz_data_salute}',
        'RqUID': str(uuid.uuid4()),
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'scope': 'SALUTE_SPEECH_PERS',
    }

    response = requests.post(url, headers=headers, data=data, verify=False)

    return response.json()['access_token']
