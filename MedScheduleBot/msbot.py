import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext

from config import TOKEN
bot = Bot(token = TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(content_types=st.NOT_TARGET_CONTENT_TYPES)
async def not_target(message: types.Message):
