from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.filters import Command
from aiogram import Dispatcher, Bot, types

from bot import keyboards
from bot.misc.env import TgKeys


bot = Bot(token=TgKeys.TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["test1"]))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

@dp.message(Command(commands=["start"]))
async def welcome(message: types.Message) -> None:
    
    await message.answer("Выберите действие")

@dp.message(Command(commands="rasp"))
async def cmd_start(message: types.Message):
    kb = [
        [
        types.KeyboardButton(text="Расписание"),
        types.KeyboardButton(text="Группа"),
        types.KeyboardButton(text="Дата"),
        types.KeyboardButton(text="Сегодня"),
        types.KeyboardButton(text="Завтра"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите нужное вам меню"
    )
    await message.answer("Что вы выбираете?", reply_markup=keyboard)

# @dp.message_handler(commands=["Расписание"])
# async def select_button1(message: types.Message):
#     await message.reply(
#         "Представьтесь. Пример: Фамилия И.О"/
#         "Это нужно для правильного получения расписания"
#         )

