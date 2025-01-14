# module 13_2
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = "" # insert your token here
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# create a keyboard
kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Информация')],
              [KeyboardButton(text='Рассчитать')]],
    resize_keyboard=True)

kb2 = InlineKeyboardMarkup()
button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
kb2.add(button_1, button_2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=kb2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer("Информация о боте!")

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
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