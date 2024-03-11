from data.loader import bot, db
from telebot.types import Message


@bot.message_handler(func=lambda message: message.text == "Ro'yhatdan o'tish")
def registeration(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "F.I.O ni kiriting: ")
    bot.register_next_step_handler(msg, get_name)


def get_name(message: Message):
    chat_id = message.chat.id
    full_name = message.text
    
