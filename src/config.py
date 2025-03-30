from dotenv import load_dotenv
import os

# Загружаем переменные из файла .env
load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')