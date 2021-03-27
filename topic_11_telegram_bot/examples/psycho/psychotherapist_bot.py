import telebot
from telebot import types

token = '1184152928:AAFvsnRFoML33KdHGu4xSx_GgQXAZrDueK0'
bot = telebot.TeleBot(token)

# {user_id: {care_cons: ..., care_pros: ..., child_needs: ..., happy_situation: .., frustration: ...}}
users_info = {}

yes_no_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
yes_no_keyboard.row("Да", "Нет")
hideBoard = types.ReplyKeyboardRemove()


@bot.message_handler(commands=['start'], content_types=['text'])
def start(message):
    bot.send_message(message.from_user.id, "Я могу помочь выявить диструктивные паттерны в отношениях. "
                                           "Просто напиши мне ответы на следующие вопросы "
                                           "(первое, что приходит в голову)")
    bot.send_message(message.from_user.id, "Согласен?", reply_markup=yes_no_keyboard)

    # следующий шаг
    bot.register_next_step_handler(message, get_care_cons)


def get_care_cons(message):
    if message.text.lower() == 'да':
        bot.send_message(message.from_user.id, "Отрицательные черты ваших значимых взрослых "
                                               "(например: жестокость, зависть, аддиктивность)", reply_markup=hideBoard)
        bot.register_next_step_handler(message, get_care_pros)
    else:
        bot.send_message(message.from_user.id, "Ок, скажешь, когда будешь готов!",  reply_markup=hideBoard)


def get_care_pros(message):
    global users_info
    users_info[message.from_user.id] = {}
    users_info[message.from_user.id]['care_cons'] = message.text
    bot.send_message(message.from_user.id, "Положительные черты ваших значимых взрослых "
                                           "(например: добрым, вежливым, щедрым)")
    bot.register_next_step_handler(message, get_child_needs)


def get_child_needs(message):
    global users_info
    users_info[message.from_user.id]['care_pros'] = message.text
    bot.send_message(message.from_user.id, "В детстве, вы больше всего нуждались, но так и не получили... "
                                           "(например: внимание, заботу, подарки)")
    bot.register_next_step_handler(message, get_happy_situation)


def get_happy_situation(message):
    global users_info
    users_info[message.from_user.id]['child_needs'] = message.text
    bot.send_message(message.from_user.id,
                     "Счастливый эпизод из детства (эмоции и потребность, что была удовлетворена)")
    bot.register_next_step_handler(message, get_frustration)


def get_frustration(message):
    global users_info
    users_info[message.from_user.id]['happy_situation'] = message.text
    bot.send_message(message.from_user.id, "Повторяющаяся фрустрация и ваша реакция на нее")
    bot.register_next_step_handler(message, get_prediction)


def get_prediction(message):
    global users_info
    users_info[message.from_user.id]['frustration'] = message.text
    result = f"Я часто ищу и нахожу человека, обладающего чертами: {users_info[message.from_user.id]['care_cons']}, " \
             f"чтобы он оказался {users_info[message.from_user.id]['care_pros']}, " \
             f"чтобы я наконец получил {users_info[message.from_user.id]['child_needs']} " \
             f"и чувствовал себя как будто {users_info[message.from_user.id]['happy_situation']}.\n\n" \
             f"Иногда, я не даю себе получить то что мне нужно, " \
             f"путем: {users_info[message.from_user.id]['frustration']}."
    bot.send_message(message.from_user.id, f"Результат:\n{result}")


@bot.message_handler(commands=['info'])
def info(message):
    send_mess_info = "Я могу лучше познать себя " + '\U0001F609'
    bot.send_message(message.chat.id, send_mess_info, parse_mode='html')


@bot.message_handler(commands=['help'])
def help_com(message):
    send_mess_help = f"<b>Привет {message.from_user.first_name}</b>!\nНапиши команду /start для начала диагностики"
    bot.send_message(message.chat.id, send_mess_help, parse_mode='html')


if __name__ == '__main__':
    print('Starting bot...')
    bot.polling(none_stop=True, interval=0)
