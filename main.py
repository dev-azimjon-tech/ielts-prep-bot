import telebot
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    logger.error("TELEGRAM_TOKEN not found in .env file")
    raise ValueError("TELEGRAM_TOKEN environment variable is required")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the IELTS Prep Bot! Use /help to see available commands.")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """Available commands:
/start - Start the bot
/help - Show this help message
/books - Browse free IELTS books
/practice - Start practice session
/resources - View free resources
/contact - Get free consultation"""
    bot.reply_to(message, help_text)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    logger.info(f"Received message from {message.from_user.first_name}: {message.text}")
    bot.reply_to(message, "Sorry, I didn't understand that. Use /help to see available commands.")

if __name__ == "__main__":
    logger.info("IELTS Prep Bot started...")
    bot.polling()