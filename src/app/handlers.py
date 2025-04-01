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


@router.message(F.text == 'Погода')
async def weather_fixed(message: Message):
    city = "Moscow"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}&units=metric"
    await send_weather(message, city, url)


@router.message()  # Обрабатываем любой текст, который не попал под другие фильтры
async def weather_by_city(message: Message):
    city = message.text.strip()  # Убираем лишние пробелы
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_API_KEY}&units=metric&lang=ru"  # Добавили lang=ru для описания на русском
    await send_weather(message, city, url)


async def send_weather(message: Message, city: str, url: str):  # Выносим логику в отдельную функцию
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()  # Получаем JSON-ответ

                # Извлекаем данные
                temperature = data['main']['temp'] # температура
                feels_like = data['main']['feels_like'] # ощущается как
                pressure = data['main']['pressure'] # давление
                humidity = data['main']['humidity'] # влажность
                weather_description = data['weather'][0]['description'] # описание погоды

                reply = (
                    f"Погода в {city} на сегодня\n"
                    "\n"
                    f"Описание: {weather_description}\n"
                    f"Температура: {round(temperature, 1)}°C (ощущается как {round(feels_like, 1)}°C)\n"
                    f"Влажность: {humidity}%\n"
                    f"Давление: {pressure} мм рт. ст."
                )

                await message.answer(reply)
            elif response.status == 404:  # Если город не найден
                await message.answer(f"Город '{city}' не найден :( \n Проверьте название и повторите запрос.")
            else:
                await message.answer("Ошибка при обращении к серверу. \n Попробуйте повторить запрос позже.")


@router.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f'Да, это фото! Его ID: {message.photo[-1].file_id}')
