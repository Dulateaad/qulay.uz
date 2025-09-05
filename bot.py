from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("8428416300:AAHTSGcXCEE5ctRDnSWS5SfZP20woRGEwkg")  # Храним токен в переменных окружения

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    webapp_btn = types.InlineKeyboardButton(
        text="Открыть приложение",
        web_app=types.WebAppInfo(url="https://studio--mening-ustozim.us-central1.hosted.app/")
    )
    keyboard.add(webapp_btn)
    await message.answer("Привет 👋 Нажми кнопку, чтобы открыть приложение:", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
