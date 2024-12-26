# module 13_2
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7477872876:AAGUniXYghKWl-x1eREG9ilnaS3mAkpcG_Y" # insert your token here
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# handler
@dp.message_handler(commands=["start"])
async def start(message):
    print("Привет! Я бот, помогающий твоему здоровью.")
    await message.answer("Рады видеть вас в нашем боте")

@dp.message_handler(text=["Привет", "Здравствуй, бот"]) # перехват 2 сообщений
async def urban_message(message):
    print("Привет!")
    await message.answer("Urban message!")

@dp.message_handler() # перехват всех сообщений
async def all_messages(message):
    print("Введите команду /start, чтобы начать сообщение.")
    await message.answer(message.text)

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)