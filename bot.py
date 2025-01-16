import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv
import os
from tables import insert_row_teble


load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)


api_token = os.getenv('API_TOKEN')


# Инициализация бота и диспетчера
bot = Bot(token=api_token)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я ваш бот. Можете написать мне вопрос который вас "
                        "интересует!!!.\nДоступные команды:\n/start - Приветствие\n/list_table - Список "
                        "Вопросов\n/help - Список команд")

# Обработчик команды /help
@dp.message(Command('help'))
async def send_help(message: types.Message):
    await message.reply("Доступные команды:\n/start - Приветствие\n/list_table - Список "
                        "Вопросов\n/help - Список команд")


# Обработчик команды /list_table
@dp.message(Command('list_table'))
async def send_help(message: types.Message):
    await message.answer("https://docs.google.com/spreadsheets/d/1Mckiqd00PwsG4oK4y5mcYf5kFEYDZswOC3GL1clLmFk/edit?hl=ru&gid=0#gid=0")


# Обработчик текстовых сообщений
@dp.message(F.text)
async def echo(message: types.Message):
    insert_row_teble(message.text)
    await message.reply(f"Ваш вопрос сохранил!!!")
