import json

import telebot
from telebot import types
from telebot.types import Message

from project.combat.body_part import BodyPart
from project.combat.game_result import GameResult
from project.combat.pokemon import Pokemon
from project.combat.pokemon_npc import PokemonNPC
from project.combat.pokemon_by_type import pokemon_by_type
from project.combat.pokemon_state import PokemonState
from project.combat.pokemon_type import PokemonType

with open("./bot_token.txt", 'r') as token_file:
    token = token_file.read().strip()

bot = telebot.TeleBot(token)

# {id: {'user_pokemon': Pokemon_obj, 'npc_pokemon': PokemonNPC_obj}}
state = {}

# {id: {'w': 0, 'l': 6, 'e': 3}, ...}
statistics = {}

stat_file = "game_stat.json"

body_part_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                               one_time_keyboard=True,
                                               row_width=len(BodyPart))

body_part_keyboard.row(*[types.KeyboardButton(body_part.name) for body_part in BodyPart])


def update_save_stat(chat_id, result: GameResult):
    print("Обновление статистики", end="...")
    global statistics

    chat_id = str(chat_id)

    if statistics.get(chat_id, None) is None:
        statistics[chat_id] = {}

    if result == GameResult.W:
        statistics[chat_id]['W'] = statistics[chat_id].get('W', 0) + 1
    elif result == GameResult.L:
        statistics[chat_id]['L'] = statistics[chat_id].get('L', 0) + 1
    elif result == GameResult.E:
        statistics[chat_id]['E'] = statistics[chat_id].get('E', 0) + 1
    else:
        print(f"Не существует результата {result}")

    with open(stat_file, 'w') as file:
        json.dump(statistics, file)

    print("завершено!")


def load_stat():
    print('Загрузка статистики...', end='')
    global statistics

    try:
        with open(stat_file, 'r') as file:
            statistics = json.load(file)
        print('завершена успешно!')
    except FileNotFoundError:
        statistics = {}
        print('файл не найден!')


@bot.message_handler(commands=["help", "info"])
def help_command(message):
    bot.send_message(message.chat.id,
                     "Hi!\n/start для начала игры\n/stat для отображения статистики")


@bot.message_handler(commands=["stat"])
def stat(message):
    global statistics
    if statistics.get(str(message.chat.id), None) is None:
        user_stat = "Еще не было ни одной игры"
    else:
        user_stat = "Твои результаты:"
        for res, num in statistics[str(message.chat.id)].items():
            user_stat += f"\n{res}: {num}"

    bot.send_message(message.chat.id,
                     text=user_stat)


@bot.message_handler(commands=["start"])
def start(message):
    yes_no_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                one_time_keyboard=True,
                                                row_width=2)
    yes_no_keyboard.row("Да", "Нет")

    bot.send_message(message.from_user.id,
                     text="Готов начать битву покемонов?",
                     reply_markup=yes_no_keyboard)

    bot.register_next_step_handler(message, start_question_handler)


def start_question_handler(message):
    if message.text.lower() == 'да':
        bot.send_message(message.from_user.id,
                         'Хорошо, начинаем!')

        create_npc(message)

        ask_user_about_pokemon_type(message)

    elif message.text.lower() == 'нет':
        bot.send_message(message.from_user.id,
                         'Ок, я подожду.')
    else:
        bot.send_message(message.from_user.id,
                         'Я не знаю такого варианта ответа!')


def create_npc(message):
    print(f"Начало создания объекта NPC для chat id = {message.chat.id}")
    global state
    pokemon_npc = PokemonNPC()
    if state.get(message.chat.id, None) is None:
        state[message.chat.id] = {}
    state[message.chat.id]['npc_pokemon'] = pokemon_npc

    npc_image_filename = pokemon_by_type[pokemon_npc.pokemon_type][pokemon_npc.name]
    bot.send_message(message.chat.id, 'Противник:')
    with open(f"../images/{npc_image_filename}", 'rb') as file:
        bot.send_photo(message.chat.id, file, pokemon_npc)
    print(f"Завершено создание объекта NPC для chat id = {message.chat.id}")


def ask_user_about_pokemon_type(message):
    markup = types.InlineKeyboardMarkup()

    # TODO: несколько кнопок в ряду
    for pokemon_type in PokemonType:
        markup.add(types.InlineKeyboardButton(text=pokemon_type.name,
                                              callback_data=f"pokemon_type_{pokemon_type.value}"))

    bot.send_message(message.chat.id, "Выбери тип покемона:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: "pokemon_type_" in call.data)
def pokemon_type_handler(call):
    call_data_split = call.data.split("_")
    if len(call_data_split) != 3 or not call_data_split[2].isdigit():
        bot.send_message(call.message.chat.id, "Возникла проблема. Перезапусти сессию!")
    else:
        pokemon_type_id = int(call_data_split[2])

        bot.send_message(call.message.chat.id, "Выбери своего покемона:")

        ask_user_about_pokemon_by_type(pokemon_type_id, call.message)


def ask_user_about_pokemon_by_type(pokemon_type_id, message):
    pokemon_type = PokemonType(pokemon_type_id)
    pokemon_dict_by_type = pokemon_by_type.get(pokemon_type, {})

    # TODO: несколько кнопок в ряду
    for pokemon_name, pokemon_img in pokemon_dict_by_type.items():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text=pokemon_name,
                                              callback_data=f"pokemon_name_{pokemon_type_id}_{pokemon_name}"))
        with open(f"../images/{pokemon_img}", 'rb') as file:
            bot.send_photo(message.chat.id, file, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: "pokemon_name_" in call.data)
def pokemon_name_handler(call):
    call_data_split = call.data.split("_")
    if len(call_data_split) != 4 or not call_data_split[2].isdigit():
        bot.send_message(call.message.chat.id, "Возникла проблема. Перезапусти сессию!")
    else:
        pokemon_type_id, pokemon_name = int(call_data_split[2]), call_data_split[3]

        create_user_pokemon(call.message, pokemon_type_id, pokemon_name)

        bot.send_message(call.message.chat.id, "Игра началась!")

        game_next_step(call.message)


def create_user_pokemon(message, pokemon_type_id, pokemon_name):
    print(f"Начало создания объекта Pokemon для chat id = {message.chat.id}")
    global state
    user_pokemon = Pokemon(name=pokemon_name,
                           pokemon_type=PokemonType(pokemon_type_id))

    if state.get(message.chat.id, None) is None:
        state[message.chat.id] = {}
    state[message.chat.id]['user_pokemon'] = user_pokemon

    image_filename = pokemon_by_type[user_pokemon.pokemon_type][user_pokemon.name]
    bot.send_message(message.chat.id, 'Твой выбор:')
    with open(f"../images/{image_filename}", 'rb') as file:
        bot.send_photo(message.chat.id, file, user_pokemon)

    print(f"Завершено создание объекта Pokemon для chat id = {message.chat.id}")


def game_next_step(message: Message):
    bot.send_message(message.chat.id,
                     "Выбор точки для защиты:",
                     reply_markup=body_part_keyboard)

    bot.register_next_step_handler(message, reply_defend)


def reply_defend(message: Message):
    if not BodyPart.has_item(message.text):
        bot.send_message(message.chat.id, "Необходимо выбрать вариант на клавиатуре!")
        game_next_step(message)
    else:
        bot.send_message(message.chat.id,
                         "Выбор точки для удара:",
                         reply_markup=body_part_keyboard)

        bot.register_next_step_handler(message, reply_attack, defend_body_part=message.text)


def reply_attack(message: Message, defend_body_part: str):
    if not BodyPart.has_item(message.text):
        bot.send_message(message.chat.id, "Необходимо выбрать вариант на клавиатуре!")
        game_next_step(message)
    else:
        attack_body_part = message.text

        global state
        # обращение по ключу ко вложенному словарю для получения объекта покемона пользователя
        user_pokemon = state[message.chat.id]['user_pokemon']

        # обращение по ключу ко вложенному словарю для получения объекта покемона npc
        pokemon_npc = state[message.chat.id]['npc_pokemon']

        # конвертировать строку хранящуюся в объекте attack_body_part в правильный тип enum BodyPart
        # конвертировать строку хранящуюся в объекте defend_body_part в правильный тип enum BodyPart
        user_pokemon.next_step_points(next_attack=BodyPart[attack_body_part],
                                      next_defence=BodyPart[defend_body_part])

        pokemon_npc.next_step_points()

        game_step(message, user_pokemon, pokemon_npc)


def game_step(message: Message, user_pokemon: Pokemon, pokemon_npc: Pokemon):
    comment_npc = pokemon_npc.get_hit(opponent_attack_point=user_pokemon.attack_point,
                                      opponent_hit_power=user_pokemon.hit_power,
                                      opponent_type=user_pokemon.pokemon_type)
    bot.send_message(message.chat.id, f"NPC pokemon: {comment_npc}\nHP: {pokemon_npc.hp}")

    comment_user = user_pokemon.get_hit(opponent_attack_point=pokemon_npc.attack_point,
                                        opponent_hit_power=pokemon_npc.hit_power,
                                        opponent_type=pokemon_npc.pokemon_type)
    bot.send_message(message.chat.id, f"Your pokemon: {comment_user}\nHP: {user_pokemon.hp}")

    if pokemon_npc.state == PokemonState.READY and user_pokemon.state == PokemonState.READY:
        bot.send_message(message.chat.id, "Продолжаем!")
        game_next_step(message)
    elif pokemon_npc.state == PokemonState.DEFEATED and user_pokemon.state == PokemonState.DEFEATED:
        bot.send_message(message.chat.id, "Ничья!")
        update_save_stat(message.chat.id, GameResult.E)
    elif pokemon_npc.state == PokemonState.DEFEATED:
        bot.send_message(message.chat.id, "Ты победил :)")
        update_save_stat(message.chat.id, GameResult.W)
    elif user_pokemon.state == PokemonState.DEFEATED:
        bot.send_message(message.chat.id, "Ты проиграл :)")
        update_save_stat(message.chat.id, GameResult.L)


if __name__ == '__main__':
    load_stat()

    print('Starting the bot...')
    bot.polling(none_stop=True, interval=0)
    print('The bot has stopped!')
