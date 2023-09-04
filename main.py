import asyncio
import logging
from config_reader import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from signup import SignUp

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()
# Подключение базы данных
signup_handler = SignUp()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    telegram_id = message.from_user.id
    race = "Default"
    player_class = "Default"

    # Check if the user is already signed up
    user = signup_handler.get_user(telegram_id)
    if not user:
        signup_handler.add_user(telegram_id, race, player_class)
        await message.answer("Welcome! You have been signed up.")
    else:
        await message.answer("You are already signed up.")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())