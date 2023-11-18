import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot('6651981565:AAHOPSZ8cNzf5DXNGBp4wXxmRve2wGdtXSA')


def phone_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Отправить контакт', request_contact=True)

    kb.add(button)

    return kb


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Привет, отправь имя чтобы начать изучать программирования)')

    bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_name = message.text
    # print(user_name)

    bot.send_message(message.from_user.id, 'Отправь контакт чтобы завершить регистрацию', reply_markup=phone_button())
    bot.register_next_step_handler(message, get_phone, user_name)


def get_phone(message, user_name):
    if message.contact:
        user_phone = message.contact.phone_number

        bot.send_message(message.from_user.id, f'Супер! Вы успешно прошли регистрацию)\nИмя: {user_name}\nNomer: {user_phone}')

    else:
        bot.send_message(message.from_user.id, 'Отправьте контакт с помощью кнопки ниже')

bot.polling()