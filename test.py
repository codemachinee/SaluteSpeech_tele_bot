from aiogram import Bot, Dispatcher, F
import asyncio
import os
from paswords import *
from api_generate import *
token = lemonade
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(F.voice, F.chat.type == 'private')
async def chek_message(v):
    await save_audio(bot, v)


async def save_audio(bot, message):
    await bot.send_message(message.chat.id, f'есть контакт')
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"{file_id}")
    url = 'https://smartspeech.sber.ru/rest/v1/speech:recognize'
    headers = {
        'Authorization': f'Bearer {key_generate()}',
        'Content-Type': 'audio/ogg;codecs=opus',
    }

    with open(f'{file_id}', 'rb') as audio_file:
        response = requests.post(url, headers=headers, data=audio_file, verify=False)
        try:
            await bot.send_message(message.chat.id, f'{" ".join(response.json()["result"])}')
            if response.json()["emotions"][0]['negative'] == max(response.json()["emotions"][0]['negative'],
                                                                 response.json()["emotions"][0]['neutral'],
                                                                 response.json()["emotions"][0]['positive']):
                await bot.send_message(message.chat.id, f'произнес как злая истеричная сучка')
            elif response.json()["emotions"][0]['positive'] == max(response.json()["emotions"][0]['negative'],
                                                                   response.json()["emotions"][0]['neutral'],
                                                                   response.json()["emotions"][0]['positive']):
                await bot.send_message(message.chat.id, f'произнес так жизнерадостно, что аж бесит')
            else:
                await bot.send_message(message.chat.id, f'произнес нормально, не докопаться')
        except Exception:
            await bot.send_message(message.chat.id, f'Ошибка. Логи:{response.json()}')
        audio_file.close()
        os.remove(f"{file_id}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
