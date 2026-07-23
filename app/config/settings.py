"""
Настройки приложения.
Читает переменные из .env.
"""

from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        self.bot_token = os.getenv("BOT_TOKEN")
        if self.bot_token is None:
            print(f'Нет {self.bot_token}')

settings = Settings()