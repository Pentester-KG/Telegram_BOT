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
async def send_photo(message: types.Message):
    file1 = types.FSInputFile('images/ilon-mask.jpg')
    file2 = types.FSInputFile('images/bill.jpg')
    file3 = types.FSInputFile('images/epic.jpg')
    file4 = types.FSInputFile('images/tim kuk.jpeg')
    file5 = types.FSInputFile('images/sam Altman.jpg')
    file6 = types.FSInputFile('images/jack ma.jpg')
    file7 = types.FSInputFile('images/jeff bezos.jpg')
    file8 = types.FSInputFile('images/ferrucho.jpg')
    file9 = types.FSInputFile('images/TASS_4205131-oleg-tinkov-in-red-front.jpg')
    file10 = types.FSInputFile('images/Warren-Buffett-01.jpg')
    all_photo = [file1, file2, file3, file4, file5, file6, file7, file8, file9, file10]
    rand_pic = random.choice(all_photo)
    await message.answer_photo(rand_pic)



async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
