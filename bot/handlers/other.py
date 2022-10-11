# здесь происходит регистрация всех функций
# из папок: database, filters, keyboards
from aiogram import Dispatcher
from aiogram import Dispatcher, Bot, types, Router
from bot.misc.env import TgKeys
from bot.keyboards.reply import cmd_start, welcome, cmd_test1
from aiogram.dispatcher.dispatcher import TelegramEventObserver

# важная фукция для регистрации хэндлеров
def register_other_handlers(dp: Dispatcher) -> None:
    dp.message.register(cmd_start)
    dp.message.register(welcome)
    dp.message.register(cmd_test1)

bot = Bot(token=TgKeys.TOKEN)
dp = Dispatcher()
rt = Router()
obs = TelegramEventObserver(router=rt, event_name=TelegramEventObserver)