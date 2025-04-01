import aiohttp

from aiogram import F, Router
from aiogram.filters import CommandStart, Command  # Импортируем классы для обработки команд
from aiogram.types import Message  # Импортируем тип Message, который представляет сообщение в Telegram

from config import OWM_API_KEY

router = Router() # Создаем экземпляр класса Router для регистрации хендлеров

@router.message(CommandStart())  # Декоратор (хендлер), который говорит, что функция ниже будет обрабатывать команду /start
async def command_start(message: Message):  # Асинхронная функция для обработки команды /start, принимает объект сообщения (Message)
    await message.reply(f"Привет, {message.from_user.first_name}! Я погодный бот. Напиши мне название города, и я покажу тебе погоду.")  # Отправляем пользователю текстовый ответ

@router.message(Command('help'))  # Декоратор (хендлер), который говорит, что функция ниже будет обрабатывать команду /help
async def command_help(message: Message):  # Асинхронная функция для обработки команды /help, принимает объект сообщения (Message)
    await message.answer("Напиши мне название города, и я покажу тебе погоду.")

@router.message(F.text == 'Погода')  # Декоратор (хендлер), функция которого будет обрабатывать текстовое сообщение 'Погода'
async def weather(message: Message):
    city = 'Moscow'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}'

    async with aiohttp.ClientSession() as session:  # Создаём сессию для запроса
        async with session.get(url) as response:
            if response.status == 200:  # Если запрос успешен
                data = await response.json()  # Получаем JSON-ответ
                await message.answer(f"Запрос норм! Вот JSON:\n{data}")
            else:
                await message.answer("Ошибка при запросе к API. Проверь ключ или попробуй повторить запрос позже.")

@router.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f'Да, это фото! Его ID: {message.photo[-1].file_id}')
