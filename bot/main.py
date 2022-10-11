# from aiogram.utils import executor
import asyncio
from aiogram import Bot, Dispatcher, types, Router
from aiogram.fsm.storage.memory import MemoryStorage
import logging

from bot.filters import register_all_filters
from bot.misc import TgKeys
from bot.handlers import register_all_handlers
from bot.database.models import register_models


async def __on_start_up() -> None:
    logging.basicConfig(level=logging.INFO)
    storage = MemoryStorage()
    bot = Bot(token=TgKeys.TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=storage)
    register_all_filters(dp)
    register_all_handlers(dp)
    register_models()
    await dp.start_polling(bot)

def start_bot():
    # dp.run_polling(bot)
    asyncio.run(__on_start_up())
    