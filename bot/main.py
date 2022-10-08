# from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import logging

from bot.filters import register_all_filters
from bot.misc import TgKeys
from bot.handlers import register_all_handlers
from bot.database.models import register_models

logging.basicConfig(level=logging.INFO)

async def __on_start_up(dp: Dispatcher) -> None:
    register_all_filters(dp)
    register_all_handlers(dp)
    register_models(dp)

def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.run_polling(bot)