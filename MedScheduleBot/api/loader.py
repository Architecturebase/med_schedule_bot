import os
import time
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from config import TABLE_ID
load_dotenv()

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

try:
    spreadsheet_id = TABLE_ID
except:
    spreadsheet_id = os.getenv("TABLE_ID")

CREDENTIALS_FILE = 'spreadsheet/credentials.json'