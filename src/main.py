

import asyncio  # Импортируем модуль asyncio для асинхронного программирования, чтобы бот мог обрабатывать запросы параллельно
import logging  # Импортируем модуль logging для ведения логов (отладочной информации о работе бота)

from aiogram import Bot, Dispatcher  # Импортируем классы Bot и Dispatcher из библиотеки aiogram для создания и управления ботом
from aiogram.filters import CommandStart  # Импортируем фильтр CommandStart для обработки команды /start
from aiogram.types import Message  # Импортируем тип Message, который представляет сообщение в Telegram

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher() # диспетчер, основной роутер

@dp.message(CommandStart())  # Декоратор (хендлер), который говорит, что функция ниже будет обрабатывать команду /start
async def command_start(message: Message):  # Асинхронная функция для обработки команды /start, принимает объект сообщения (Message)
    await message.answer("Привет! Я погодный бот. Напиши мне название города, и я покажу тебе погоду.")  # Отправляем пользователю текстовый ответ

async def main():  # Асинхронная функция main, которая запускает бота
    await dp.start_polling(bot)  # Запускаем процесс опроса серверов Telegram для получения обновлений (сообщений) и передаём ему объект бота

if __name__ == '__main__':
    print('Bot started!') 
    logging.basicConfig(level=logging.INFO) # логируем всё, что происходит в боте
    try:
        asyncio.run(main())
    except KeyboardInterrupt: # остановка бота без ошибок
        print('Bot stopped!')