from pyrogram import Client, filters
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask
import threading

load_dotenv(find_dotenv())

# Replace these with your own values
api_id = os.environ.get("TELEGRAM_API_ID")
api_hash = os.environ.get("TELEGRAM_API_HASH")
bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
port = int(os.environ.get("PORT", 10000))  # Default to 10000 if PORT is not set

# Initialize the Pyrogram client
app_tg = Client("mom_ai_tg_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app_tg.on_message(filters.command("start"))
async def get_chat_id(client, message):
    chat_id = message.chat.id
    await message.reply('Hi! Please insert the code provided below on your account dashboard in the section Profile -> Notifications on mom-ai-restaurant.pro\n\nAfter the insertion MOM AI Restaurant Assistant will send the notifications in this chat upon the arrival of successfully paid orders!')
    await message.reply('The code to insert:')
    await message.reply(f'{chat_id}')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is the Pyrogram bot server running!'

# Function to run the Pyrogram bot
def run_bot():
    app_tg.run()

# Function to run the Flask server
def run_flask():
    app.run(host='0.0.0.0', port=port)

# Run both Flask server and Pyrogram bot in separate threads
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    threading.Thread(target=run_flask).start()

