from json import load
from lib2to3.pgen2 import token
import os
from dotenv import load_dotenv
from typing import Final
from aiogram import Bot

# получение конфигов из .env
class TgKeys:
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv()
    TOKEN: Final = os.environ.get('token')
    