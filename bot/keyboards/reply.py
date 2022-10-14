from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command, Text
from aiogram import Dispatcher, Bot, types
from magic_filter import F
from bot import keyboards
from bot.misc.env import TgKeys


bot = Bot(token=TgKeys.TOKEN)
dp = Dispatcher()


def rasp_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Завтра")
    kb.button(text="Сегодня")
    # kb.adjust(3)
    kb.button(text="Расписание")
    kb.button(text="Группа")
    kb.button(text="Дата")
    kb.adjust(2,3, repeat=False)
    return kb.as_markup(resize_keyboard=True)