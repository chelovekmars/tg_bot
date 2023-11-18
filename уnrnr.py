import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot('6651981565:AAHOPSZ8cNzf5DXNGBp4wXxmRve2wGdtXSA')


def main_menu_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    button1 = KeyboardButton('Контакты')
    button2 = KeyboardButton('Каталог')
    button3 = KeyboardButton('Адресс')
    button4 = KeyboardButton('Почта')

    kb.row(button2)
    kb.add(button1, button4, button3)

    return kb


def catalog_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    catalog = ['Телефоны', 'Акссесуары', 'ПК', 'Одежды для электроники']

    for i in catalog:
        kb.add(KeyboardButton(i))

    return kb


# Обработываем команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    text = f'Hello {message.from_user.first_name}!\nWelcome to our bot)))'

    bot.send_message(message.from_user.id, text, reply_markup=main_menu_button())

    print(message.from_user.id)


@bot.message_handler(commands=['qrcode'])
def qrcode_command(message):
    with open('./qr_code.png', 'rb') as qr_photo:
        bot.send_photo(message.from_user.id, qr_photo)


# Обработываем текст
@bot.message_handler(content_types=['text'])
def echo(message):

    # bot.send_message(message.from_user.id, message.text)
    # print(message.text)

    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет, Чем могу помочь?')

    elif message.text.lower() == 'кто тебя создал':
        bot.send_message(message.from_user.id, 'Меня создал компания GAGAIT')

    elif message.text.lower() == 'qrcode':
        with open('./qr_code.png', 'rb') as qr_photo:
            bot.send_photo(message.from_user.id, qr_photo)


    elif message.text == 'Контакты':
        bot.send_message(message.from_user.id, 'Наш кантакт: +998907777777')

    elif message.text == 'Каталог':
        bot.send_message(message.from_user.id, 'Выберите категорию ниже', reply_markup=catalog_buttons())

    elif message.text == 'Телефоны':
        bot.send_message(message.from_user.id, 'Phone: Iphone 14 pro max\nColor: Black\nMemory: 128 gb\nPrice: 1200$')

# обработка фотографии
@bot.message_handler(content_types=['photo'])
def photo_message(message):

    file = message.photo[-1].file_id
    print(file)

    bot.send_photo(message.from_user.id, file)



# обработка стикеров
@bot.message_handler(content_types=['sticker'])
def sticker_message(message):

    sticker = message.sticker.file_id
    print(sticker)
    bot.send_sticker(message.from_user.id, sticker)


# обработка видео файлов
@bot.message_handler(content_types=['video'])
def video_message(message):
    video = message.video.file_id

    bot.send_video(message.from_user.id, video)


@bot.message_handler(content_types=['audio'])
def audio_message(message):
    audio = message.audio.file_id
    bot.send_audio(message.from_user.id, audio)




# запускает бот
bot.polling()