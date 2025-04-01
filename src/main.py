

import asyncio  # Импортируем модуль asyncio для асинхронного программирования, чтобы бот мог обрабатывать запросы параллельно
import logging  # Импортируем модуль logging для ведения логов (отладочной информации о работе бота)

from aiogram import Bot, Dispatcher, F # Импортируем классы из библиотеки aiogram для создания и управления ботом
from aiogram.filters import CommandStart, Command  # Импортируем классы для обработки команд
from aiogram.types import Message  # Импортируем тип Message, который представляет сообщение в Telegram

from config import TG_BOT_TOKEN, OWM_API_KEY

bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher() # диспетчер, основной роутер

@dp.message(CommandStart())  # Декоратор (хендлер), который говорит, что функция ниже будет обрабатывать команду /start
async def command_start(message: Message):  # Асинхронная функция для обработки команды /start, принимает объект сообщения (Message)
    await message.answer(f"Привет, {message.from_user.first_name}! Я погодный бот. Напиши мне название города, и я покажу тебе погоду.")  # Отправляем пользователю текстовый ответ

@dp.message(Command('help'))  # Декоратор (хендлер), который говорит, что функция ниже будет обрабатывать команду /help
async def command_help(message: Message):  # Асинхронная функция для обработки команды /help, принимает объект сообщения (Message)
    await message.answer("Напиши мне название города, и я покажу тебе погоду.")

@dp.message(F.text == 'Погода')  # Декоратор (хендлер), который говорит, что функция ниже будет обрабатывать текстовые сообщения
async def weather(message: Message):
    await message.answer('Да, это погода!')

@dp.message(F.photo)
async def photo(message: Message):
    await message.answer(f'Да, это фото! Его ID: {message.photo[-1].file_id}')

async def main():  # Асинхронная функция main, которая запускает бота
    await dp.start_polling(bot)  # Запускаем процесс опроса серверов Telegram для получения обновлений (сообщений) и передаём ему объект бота

if __name__ == '__main__':
    print('Bot started!') 
    logging.basicConfig(level=logging.INFO) # логируем всё, что происходит в боте
    try:
        asyncio.run(main())
    except KeyboardInterrupt: # остановка бота без ошибок
        print('Bot stopped!')