from email import message
import imp
from aiogram import Bot, types, Dispatcher, executor

from config import TOKEN

import markup as nav

import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет", reply_markup = nav.mainMenu)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я ничем не могу тебе помочь!")

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == ('Рандомное число'):
        await bot.send_message(message.from_user.id, 'Ваше число ' + str(random.randint(1, 100)))
    elif message.text == ('Другое'):
        await bot.send_message(message.from_user.id, 'Что-то другое')

if __name__ == '__main__':
    executor.start_polling(dp)