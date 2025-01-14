# module 13_2
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = "" # insert your token here
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# create a keyboard
kb = ReplyKeyboardMarkup(resize_keyboard=True)
# create a button
button_1 = KeyboardButton(text='Информация')
button_2 = KeyboardButton(text='Рассчитать')
# add buttons to the keyboard
kb.add(button_1, button_2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=kb)

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer("Информация о боте!")

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    # count for women
    A = 1.55
    x = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161) * A
    await message.answer(f"Ваша норма калорий {x}")
    await state.finish()

@dp.message_handler() # перехват всех сообщений
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать сообщение.")

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)