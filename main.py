import asyncio
import logging
from config_reader import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from signup import SignUp
from message_handlers_main import cmd_start

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()
# Подключение базы данных
signup_handler = SignUp()

# register start message handler
dp.message.register(cmd_start, Command("start"))

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())