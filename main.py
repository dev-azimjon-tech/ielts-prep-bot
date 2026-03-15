import telebot
from dotenv import load_dotenv
import os
import logging
from telebot import types
import json


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

USERS_FILE = "users.json"
BOOKS_FILE = "books.json"


if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
else:
    users = {}

def save_users():
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        books = json.load(f)
else:
    books = {}

def save_books():
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=2)

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
    buttons = [types.KeyboardButton(book['name']) for book in books]
    markup_books.add(*buttons)
    bot.send_message(message.chat.id, "Choose the book you want: ", reply_markup=markup_books)


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