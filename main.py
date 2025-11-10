import asyncio
import logging
import os

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import Command, CommandStart
from dotenv import load_dotenv


load_dotenv('.env')
BOT_TOKEN = os.getenv('BOT_API_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f'Hello, {message.from_user.full_name}')

@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm your bot.\nSend me any message"
    await message.answer(text=text)

@dp.message()
async def echo_message(message: types.Message):

    await message.answer(text="Wait a second...")
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply("something new)))")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
