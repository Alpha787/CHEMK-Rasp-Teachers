from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.router import Router
from aiogram import Dispatcher, Bot, types

from bot import keyboards
from bot.misc.env import TgKeys


bot = Bot(token=TgKeys.TOKEN)
dp = Dispatcher()
# router = Router()

# определяются кнопки бота
# FIXME: сделать рефакторинг данного блока до ф-ии select_button1
# button1 = KeyboardButton("Расписание")
# button2 = KeyboardButton("Группа")
# button3 = KeyboardButton("Дата")
# button4 = KeyboardButton("Сегодня")
# button5 = KeyboardButton("Завтра")
# keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
#                                 row(button4, button5).row(button1,button2, button3)

@dp.message(Command(commands=["start"]))
async def welcome(message: types.Message) -> None:
    
    await message.answer("Выберите действие")


# @dp.message_handler(commands=["Расписание"])
# async def select_button1(message: types.Message):
#     await message.reply(
#         "Представьтесь. Пример: Фамилия И.О"/
#         "Это нужно для правильного получения расписания"
#         )

