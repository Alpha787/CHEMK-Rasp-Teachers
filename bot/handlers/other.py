from aiogram import Dispatcher
from aiogram.types import Message

from aiogram import Dispatcher, Bot, types
from aiogram.utils import executor
from bot.misc.env import TgKeys

import logging
from random import randint

async def echo(msg: Message):
    await msg.answer(msg.text)

def register_other_handlers(dp: Dispatcher) -> None:
    # dp.register_message_handler(echo, content_types=["text"])
    dp.register_message_handler(print_random_number_for_start)
    

bot = Bot(token=TgKeys.TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def print_random_number_for_start(message: types.Message):
    """
    This handler will print random number from 1 to 10 ask for "/start"
    """
    await message.reply(f"Fuck off {randint(0, 10)}")
    # print(randint(0, 10))