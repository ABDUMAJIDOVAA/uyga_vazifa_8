from data.loader import bot, db
from telebot.types import Message
from keyboards.default import register


@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    check = db.chek_user(telegram_id=from_user_id)
    if None in check:
        bot.send_message(chat_id, "Translate botga xush kelibsiz.\n")

    db.insert_telegram_id(telegram_id=from_user_id)

    check = db.chek_user(telegram_id=from_user_id)
    if None in none:
        bot.send_message(chat_id, "Translate botga xush kelibsiz.\n"
                                    "Botdan foydalinish uchunroyxatdan oting", reply_markup=register())

    
    