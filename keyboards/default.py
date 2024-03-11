from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def register():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("Ro'yhatdan o'tish")
    markup.add(btn1)
    return markup