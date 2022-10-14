import logging
from unicodedata import name
from aiogram import Router, F, html
from aiogram.filters import Text, Command
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from bot.keyboards.reply import rasp_keyboard

router = Router()

class Form(StatesGroup):
    name = State()
    like_bots = State()
    language = State()

@router.message(Command(commands="start"))
async def cmd_help(message: Message):
    await message.answer(
        "Выберите нужное вам меню",
        reply_markup=rasp_keyboard()
    )

@router.message(Command(commands="cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info(f"Cancelling state {current_state}")
    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )

@router.message(Text(text="Расписание", ignore_case=True))
async def raspisanie(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(
        "Представьтесь.\nПример: Фамилия И.О\n"
        "Это нужно для правильного получения расписания",
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.like_bots)
    await message.answer(
        f"Nice to meet you, {html.quote(message.text)}!\nDid you like it>",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Yes"),
                    KeyboardButton(text="No"),
                ]
            ],
            resize_keyboard=True
        ),
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