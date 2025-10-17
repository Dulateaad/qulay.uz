import logging
from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Вставь свой токен
BOT_TOKEN = "8428416300:AAHTSGcXCEE5ctRDnSWS5SfZP20woRGEwkg"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("Открыть приложение", web_app=WebAppInfo(url="https://studio--studio-209476327-befec.us-central1.hosted.app/"))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Привет! 👋 Нажми кнопку ниже, чтобы открыть приложение:",
        reply_markup=reply_markup
    )

# Обработка текстов
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Ты написал: {update.message.text}")

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Хендлеры
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запуск
    application.run_polling()

if __name__ == "__main__":
    main()
