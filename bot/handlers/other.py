# здесь происходит регистрация всех функций
# из папок: database, filters, keyboards
from aiogram import Dispatcher
from aiogram import Dispatcher, Bot, types
from bot.misc.env import TgKeys
from bot.keyboards.reply import welcome
# from bot.keyboards.reply import select_button1

# важная фукция для регистрации хэндлеров
def register_other_handlers(dp: Dispatcher) -> None:
    # dp.register_message_handler(echo, content_types=["text"])
    # dp.register_message_handler(print_random_number_for_start)
    # dp.register_message_handler(reply_keyboard_buttons)
    dp.register_message_handler(welcome)
    # dp.register_message_handler(select_button1)
    # bot.set_chat_menu_button(chat_menu)

bot = Bot(token=TgKeys.TOKEN)
dp = Dispatcher()
