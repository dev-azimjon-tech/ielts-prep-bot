import telebot
from dotenv import load_dotenv
import os
import logging
from telebot import types

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()


TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    logger.error("TELEGRAM_TOKEN not found in .env file")
    raise ValueError("TELEGRAM_TOKEN environment variable is required")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def register_user(message):
    markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_main.add(
        types.KeyboardButton("Browse Free IELTS Books"),
        types.KeyboardButton("Start Practice Session"),
        types.KeyboardButton("View Free Resources"),
        types.KeyboardButton("Get Free Consultation"),
        types.KeyboardButton("Contact Support"),
        types.KeyboardButton("Premium Subscription")
    )

    bot.reply_to(message, "Welcome to the IELTS Prep Bot! Use /help to see available commands.", reply_markup=markup_main)


@bot.message_handler(func=lambda message: message.text == "Browse Free IELTS Books")
def browse_books(message):
    markup_books = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_books.add(
        types.KeyboardButton("Book 1"),
        types.KeyboardButton("Book 2"),
        types.KeyboardButton("Book 3"),
        types.KeyboardButton("Book 4")
    )
    bot.send_message(message.chat.id, "Choose the book you want: ", reply_markup=markup_books)


# Add /books command handler to trigger browse_books
@bot.message_handler(commands=['books'])
def books_command(message):
    browse_books(message)


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