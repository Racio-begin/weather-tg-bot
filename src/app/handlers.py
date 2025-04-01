from aiogram import F, Router
from aiogram.filters import CommandStart, Command  # Импортируем классы для обработки команд
from aiogram.types import Message  # Импортируем тип Message, который представляет сообщение в Telegram

router = Router() # Создаем экземпляр класса Router для регистрации хендлеров

@router.message(CommandStart())  # Декоратор (хендлер), который говорит, что функция ниже будет обрабатывать команду /start
async def command_start(message: Message):  # Асинхронная функция для обработки команды /start, принимает объект сообщения (Message)
    await message.reply(f"Привет, {message.from_user.first_name}! Я погодный бот. Напиши мне название города, и я покажу тебе погоду.")  # Отправляем пользователю текстовый ответ

@router.message(Command('help'))  # Декоратор (хендлер), который говорит, что функция ниже будет обрабатывать команду /help
async def command_help(message: Message):  # Асинхронная функция для обработки команды /help, принимает объект сообщения (Message)
    await message.answer("Напиши мне название города, и я покажу тебе погоду.")

@router.message(F.text == 'Погода')  # Декоратор (хендлер), который говорит, что функция ниже будет обрабатывать текстовые сообщения
async def weather(message: Message):
    await message.answer('Да, это погода!')

@router.message(F.photo)
async def photo(message: Message):
    await message.answer(f'Да, это фото! Его ID: {message.photo[-1].file_id}')
