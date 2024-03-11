import telebot
import qrcode
from io import BytesIO

TOKEN = '7012019536:AAGOam0l-3yq72__ukDgb9P2uFiiJctKsQU'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Menga URL yoki biror bir silka yubor.")

@bot.message_handler(func=lambda message: True)
def send_qr(message):
    text = message.text
    if text.startswith('http'):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        bio = BytesIO()
        bio.name = 'image.png'
        img.save(bio, 'PNG')
        bio.seek(0)
        bot.send_photo(message.chat.id, photo=bio)
        bot.reply_to(message, "QR kod tayyor!")
    else:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        bio = BytesIO()
        bio.name = 'image.png'
        img.save(bio, 'PNG')
        bio.seek(0)
        bot.send_photo(message.chat.id, photo=bio)
        bot.reply_to(message, "QR kod muvaffaqiyatli yaratildi!")

bot.polling()


""" echo "# uyga_vazifa_8" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ABDUMAJIDOVAA/uyga_vazifa_8.git
git push -u origin main """