import telebot
from telebot import types
from topic_11_telegram_bot.examples.cats.cat_breeds_info import *

token = '1184152928:AAFvsnRFoML33KdHGu4xSx_GgQXAZrDueK0'
bot = telebot.TeleBot(token)


def get_formatted_answer_str(answer_dict):
    return "Size: {Size}\n\nColor: {Color}\n\nInfo: {Info}".format(**answer_dict)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Exotic Shorthair', callback_data=1))
    markup.add(types.InlineKeyboardButton(text='Manx', callback_data=2))
    markup.add(types.InlineKeyboardButton(text='Siberian', callback_data=3))

    # Без использования html
    send_mess_start = f"Привет {message.from_user.first_name}!\nО какой кошке ты хочешь узнать?"
    bot.send_message(message.chat.id, send_mess_start, reply_markup=markup)

    # С использованием html
    # send_mess_start = f"<b>Привет {message.from_user.first_name}</b>!\nО какой кошке ты хочешь узнать?"
    # bot.send_message(message.chat.id, send_mess_start, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Краткая информация')
    answer = ''
    img = ''
    if call.data == '1':
        answer = get_formatted_answer_str(exotic_shorthair)
        img = 'img/Exotic Shorthair Cat Breed.jpg'
    elif call.data == '2':
        answer = get_formatted_answer_str(manx)
        img = 'img/Manx Cat.jpg'
    elif call.data == '3':
        answer = get_formatted_answer_str(siberian)
        img = 'img/Siberian Cat Breed.jpg'

    if img:
        img = open(img, 'rb')
        bot.send_photo(call.message.chat.id, img, answer)
        img.close()
    else:
        bot.send_message(call.message.chat.id, answer)


@bot.message_handler(commands=['info'])
def info(message):
    send_mess_info = 'Я могу рассказать о нескольких <b>видах котиков</b>.' \
                     '\nВы можете управлять мной, отправив эти команды:\n' \
                     '\n/start - запуск бота и отображение списка котиков' \
                     '\n/help - расскажет как запустить бота'

    bot.send_message(message.chat.id, send_mess_info, parse_mode='html')


@bot.message_handler(commands=['help'])
def help_com(message):
    send_mess_help = f"<b>Привет {message.from_user.first_name}</b>!\nНапиши команду /start"
    bot.send_message(message.chat.id, send_mess_help, parse_mode='html')


if __name__ == '__main__':
    print('Starting bot...')
    bot.polling(none_stop=True, interval=0)
