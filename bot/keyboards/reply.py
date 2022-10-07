from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from aiogram import Dispatcher, Bot, types
from aiogram.utils import executor
from bot import keyboards
from bot.misc.env import TgKeys


bot = Bot(token=TgKeys.TOKEN)
dp = Dispatcher(bot)

# определяются кнопки бота
# FIXME: сделать рефакторинг данного блока до ф-ии Welcome
button1 = KeyboardButton("Расписание")
button2 = KeyboardButton("Группа")
button3 = KeyboardButton("Дата")
button4 = KeyboardButton("Сегодня")
button5 = KeyboardButton("Завтра")
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
                                row(button4, button5).row(button1,button2, button3)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Выберите действие", reply_markup=keyboard1)
