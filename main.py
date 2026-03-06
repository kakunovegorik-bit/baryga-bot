import logging
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ParseMode

API_TOKEN = 'YOUR_BOT_API_TOKEN'
ADMIN_ID = 'YOUR_ADMIN_ID'  # Replace with the actual admin user ID

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Database setup
def db_setup():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS activity (
            user_id INTEGER,
            activity TEXT,
            timestamp TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
    ''')
    conn.commit()
    conn.close()

# Log user activity
def log_user_activity(user_id, activity):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO activity (user_id, activity, timestamp) VALUES (?, ?, ?)', (user_id, activity, datetime.now().isoformat()))
    conn.commit()
    conn.close()

# Start command handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! Please choose an option:", reply_markup=main_menu())

# Main menu buttons
def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Buy UC", callback_data="buy_uc"))
    markup.add(InlineKeyboardButton("Popularity", callback_data="popularity"))
    markup.add(InlineKeyboardButton("Rights", callback_data="rights"))
    markup.add(InlineKeyboardButton("Promos", callback_data="promos"))
    markup.add(InlineKeyboardButton("Information", callback_data="information"))
    markup.add(InlineKeyboardButton("Referral", callback_data="referral"))
    return markup

# Handle user messages
@dp.message_handler(content_types=['text', 'photo'])
async def handle_message(message: types.Message):
    log_user_activity(message.from_user.id, message.content_type)
    if message.content_type == 'photo':
        await bot.send_message(ADMIN_ID, f"Received photo from {message.from_user.id}")
    await message.reply("Message received!")

# Handle callback queries
@dp.callback_query_handler(lambda c: True)
async def process_callback(callback_query: types.CallbackQuery):
    code = callback_query.data
    # Placeholder for processing different options
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"You selected: {code}")

if __name__ == '__main__':
    db_setup()
    executor.start_polling(dp, skip_updates=True)