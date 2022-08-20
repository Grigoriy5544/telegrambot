import imp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnRandom = KeyboardButton('Рандомное число')
btnOther = KeyboardButton('Другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnOther)