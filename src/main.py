

import asyncio  # Импортируем модуль asyncio для асинхронного программирования, чтобы бот мог обрабатывать запросы параллельно
import logging  # Импортируем модуль logging для ведения логов (отладочной информации о работе бота)

from aiogram import Bot, Dispatcher # Импортируем классы из библиотеки aiogram для создания и управления ботом

from config import TG_BOT_TOKEN
from app.handlers import router

bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher() # диспетчер, основной роутер

async def main():  # Асинхронная функция main, которая запускает бота
    dp.include_router(router) # Вызываем метод include_router() для включения роутера в диспетчер
    await dp.start_polling(bot)  # Запускаем процесс опроса серверов Telegram для получения обновлений (сообщений) и передаём ему объект бота

if __name__ == '__main__':
    print('Bot started!') 
    logging.basicConfig(level=logging.INFO) # логируем всё, что происходит в боте
    try:
        asyncio.run(main())
    except KeyboardInterrupt: # остановка бота без ошибок
        print('Bot stopped!')