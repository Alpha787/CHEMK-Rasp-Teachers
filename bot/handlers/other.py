# здесь происходит регистрация всех функций
# из папок: database, filters, keyboards
from aiogram import Dispatcher
from aiogram import Dispatcher, Bot, types, Router
from aiogram.filters import Text, Command
from magic_filter import F
from bot.misc.env import TgKeys
from bot.keyboards.reply import cmd_start, cmd_test1, select_button1, select_group
from aiogram.dispatcher.dispatcher import TelegramEventObserver

# важная фукция для регистрации хэндлеров
def register_other_handlers(dp: Dispatcher) -> None:
    dp.message.register(cmd_start)
    # dp.message.register(welcome)
    dp.message.register(cmd_test1)
    dp.message.register(select_button1)
    dp.message.register(select_group)

bot = Bot(token=TgKeys.TOKEN)
dp = Dispatcher()
rt = Router()
obs = TelegramEventObserver(router=rt, event_name=TelegramEventObserver)