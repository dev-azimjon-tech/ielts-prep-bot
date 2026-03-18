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
def menu(message):
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


# Books
@bot.message_handler(func=lambda message: message.text == "Browse Free IELTS Books")
def browse_books(message):
    markup_books = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [types.KeyboardButton(book['name']) for book in books]
    markup_books.add(*buttons, types.KeyboardButton("Back to Main Menu"))
    bot.send_message(message.chat.id, "Choose the book you want: ", reply_markup=markup_books)


@bot.message_handler(commands=['books'])
def books_command(message):
    browse_books(message)


# Practise
@bot.message_handler(func=lambda message: message.text == "Start Practice Session")
def start_practice(message):
    bot.reply_to(message, "Starting practice session...")





# Resources
@bot.message_handler(func=lambda message: message.text == "View Free Resources")
def view_resources(message):
    markup_resources = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_resources.add(
        types.KeyboardButton("IELTS Practice Tests"),
        types.KeyboardButton("IELTS Tips and Strategies"),
        types.KeyboardButton("IELTS Vocabulary Lists"),
        types.KeyboardButton("IELTS Writing Samples"),
        types.KeyboardButton("IELTS Speaking Topics"),
        types.KeyboardButton("Back to Main Menu")
    )
    bot.send_message(message.chat.id, "Choose a resource: ", reply_markup=markup_resources)

@bot.message_handler(func=lambda message: message.text == "IELTS Practice Tests")
def ielts_practice_tests(message):
    markup_tests = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_tests.add(
        types.KeyboardButton("Download Practice Tests"),
        types.KeyboardButton("Back to Resources Menu")
    )
    bot.reply_to(message, "Here are some IELTS practice tests you can try!\n \n1. [IELTS Practice Test 1](https://www.ielts.org/about-ielts/ielts-sample-test-questions)\n2. [IELTS Practice Test 2](https://www.ieltsbuddy.com/ielts-practice-tests.html)\n3. [IELTS Practice Test 3](https://www.examenglish.com/IELTS/IELTS_practice_tests.html)", reply_markup=markup_tests, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "IELTS Tips and Strategies")
def ielts_tips(message):
    markup_tips = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_tips.add(
        types.KeyboardButton("Back to Resources Menu")
    )
    bot.reply_to(message, "Here are some tips and strategies for IELTS preparation:\n\n1. Understand the test format and requirements.\n2. Practice regularly with sample questions.\n3. Focus on improving your English language skills.\n4. Take timed practice tests to build stamina.\n5. Review your mistakes and learn from them.\n6. Use official IELTS preparation materials.", reply_markup=markup_tips)

@bot.message_handler(func=lambda message: message.text == "IELTS Vocabulary Lists")
def ielts_vocabulary(message):
    markup_vocab = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_vocab.add(
        types.KeyboardButton("Download Vocabulary Lists"),
        types.KeyboardButton("Back to Resources Menu")
    )
    bot.reply_to(message, "Here are some useful IELTS vocabulary lists:\n\n1. [IELTS Vocabulary List 1](https://www.ieltsbuddy.com/ielts-vocabulary-list.html)\n2. [IELTS Vocabulary List 2](https://www.examenglish.com/IELTS/IELTS_vocabulary.html)\n3. [IELTS Vocabulary List 3](https://www.ieltsliz.com/ielts-vocabulary/)", reply_markup=markup_vocab, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "IELTS Writing Samples")
def ielts_writing_samples(message):
    markup_writing = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_writing.add(
        types.KeyboardButton("Download Writing Samples"),
        types.KeyboardButton("Back to Resources Menu")
    )
    bot.reply_to(message, "Here are some IELTS writing samples:\n\n1. [IELTS Writing Samples 1](https://www.ieltsbuddy.com/ielts-writing-samples.html)\n2. [IELTS Writing Samples 2](https://www.examenglish.com/IELTS/IELTS_writing_samples.html)\n3. [IELTS Writing Samples 3](https://www.ieltsliz.com/ielts-writing-task-2-sample-answers/)", reply_markup=markup_writing, parse_mode='Markdown')


@bot.message_handler(func=lambda message: message.text == "IELTS Speaking Topics")
def ielts_speaking_topics(message):
    markup_speaking = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_speaking.add(
        types.KeyboardButton("Download Speaking Topics"),
        types.KeyboardButton("Back to Resources Menu")
    )
    bot.reply_to(message, "Here are some IELTS speaking topics:\n\n1. [IELTS Speaking Topics 1](https://www.ieltsbuddy.com/ielts-speaking-topics.html)\n2. [IELTS Speaking Topics 2](https://www.examenglish.com/IELTS/IELTS_speaking_topics.html)\n3. [IELTS Speaking Topics 3](https://www.ieltsliz.com/ielts-speaking-topics/)", reply_markup=markup_speaking, parse_mode='Markdown')


@bot.message_handler(func=lambda message: message.text == "Back to Resources Menu")
def back_to_resources_menu(message):
    view_resources(message)

# Help
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


@bot.message_handler(func=lambda message: message.text == "Back to Main Menu")
def back_to_main_menu(message):
    menu(message)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    logger.info(f"Received message from {message.from_user.first_name}: {message.text}")
    bot.reply_to(message, "Sorry, I didn't understand that. Use /help to see available commands.")

if __name__ == "__main__":
    logger.info("IELTS Prep Bot started...")
    bot.polling()