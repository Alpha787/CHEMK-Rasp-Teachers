from aiogram import Router
from aiogram.filters import Text, Command
from aiogram.types import Message, ReplyKeyboardRemove
from bot.keyboards.reply import get_rasp

router = Router()

@router.message(Command(commands="start"))
async def cmd_help(message: Message):
    await message.answer(
        "Выберите нужное вам меню",
        reply_markup=get_rasp()
    )

@router.message(Text(text="Расписание", ignore_case=True))
async def raspisanie(message: Message):
    await message.answer(
        "Представьтесь.\nПример: Фамилия И.О\n"
        "Это нужно для правильного получения расписания",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(Text(text="Группа", ignore_case=True))
async def group(message: Message):
    await message.answer(
        "Вывод группы",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(Text(text="Дата", ignore_case=True))
async def date(message: Message):
    await message.answer(
        "Вывод даты",
        reply_markup=ReplyKeyboardRemove()
    )