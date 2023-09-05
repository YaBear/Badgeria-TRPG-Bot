from aiogram import types
from aiogram.filters.command import Command
from signup import SignUp

signup_handler = SignUp()

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