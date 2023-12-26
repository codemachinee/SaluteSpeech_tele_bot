from aiogram import Bot, Dispatcher, F
import asyncio
import os
from paswords import *
from api_generate import *
token = lemonade
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(F.text)
async def chek_message(message):
    try:
        if message.reply_to_message.voice.file_id:
            print(True)
    except AttributeError:
        print(False)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')