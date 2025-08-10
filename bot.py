# bot.py
import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Загружаем переменные окружения (только для локального запуска)
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Получаем токен
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN не найден. Установите его в .env или в переменных среды.")

# Обработчик /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я философский бот.\n"
        "Задай любой вопрос — постараюсь ответить на основе знаний."
    )

# Временный обработчик сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    logger.info(f"Сообщение от {user.full_name}: {text}")

    await update.message.reply_text(
        f"📩 Я получил ваш вопрос: *{text}*\n\n"
        "Скоро я научусь отвечать по-настоящему, используя философские тексты.",
        parse_mode='Markdown'
    )

# Основная функция
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("✅ Бот запущен и слушает обновления...")
    app.run_polling()

if __name__ == "__main__":
    main()