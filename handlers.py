#Import library
from main import bot, dp
from aiogram import types
from aiogram.types import Message
import pymysql
from config import dbHost, dbUser, dbPassword, dbName

#Keyboard bot
keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

#Connecton to database from config.pe file
connection = pymysql.connect(host=dbHost, user=dbUser, password=dbPassword, database=dbName)

#Array for keyboard
array_keyboard = [1,2]

#Send message to admin
async def send_to_admin(dp):
    await bot.send_message(chat_id=888881913, text="Bot start")

# Function of start bot
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
    await message.answer(text="Hello!", reply_markup=keyboard_markup)
    analytic(message.from_user.username, message.from_user.id, message.from_user.full_name, message.text)

def analytic(nickname, tgid, fullname, command):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users(user_nickname, user_tgid, user_fullname, user_command) VALUES ('%s', '%s', '%s', '%s')" % (nickname, tgid, fullname, command))
    connection.commit()
    cursor.close()