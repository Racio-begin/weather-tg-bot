from dotenv import load_dotenv
import os

# Загружаем переменные из файла .env
load_dotenv()

TG_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OWM_API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')