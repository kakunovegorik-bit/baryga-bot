import sqlite3
import telebot
from telebot import types

# Constants
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
ADMIN_CHAT_ID = '@dddltasa'

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Database setup
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    last_name TEXT
)
''')
conn.commit()

# Commands
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to BARYGA, your PUBG UC bot!")
    log_user(message)

@bot.message_handler(commands=['help'])
def help_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('/start', '/info', '/menu', '/admin')
    bot.send_message(message.chat.id, "Here are the commands you can use:", reply_markup=markup)


def log_user(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    cursor.execute('INSERT OR IGNORE INTO users (user_id, username, first_name, last_name) VALUES (?, ?, ?, ?)',
                   (user_id, username, first_name, last_name))
    conn.commit()

@bot.message_handler(commands=['menu'])
def menu_command(message):
    bot.send_message(message.chat.id, "Menu: \n1. Get UC \n2. Admin Notifications")

@bot.message_handler(commands=['admin'])
def admin_command(message):
    if message.from_user.username == 'your_admin_username':
        bot.send_message(ADMIN_CHAT_ID, "Admin command executed!")
    else:
        bot.send_message(message.chat.id, "You are not authorized to access admin commands.")

if __name__ == '__main__':
    bot.polling()