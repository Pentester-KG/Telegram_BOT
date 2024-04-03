import asyncio
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
import os

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


# handlers
@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer(f'Привет!, {message.from_user.first_name}')


@dp.message(Command('myinfo'))
async def myinfo_cmd(message: types.Message):
    user = message.from_user
    info_message = f'Ваш id: {user.id}\nВаше имя: {user.first_name}\n'
    if user.username:
        info_message += f'Ваш никнейм: @{user.username}'
    await message.answer(info_message)


@dp.message(Command('picture'))
async def send_picture(message: types.Message):
    img_dir = 'images'
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, random.choice(img_list))
    file = types.FSInputFile(img_path)
    await message.answer_photo(photo=file)




async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
