from keyboa import Keyboa
from telebot import TeleBot, types
from TOKEN import token
from pieces import *
from game import *

bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def greet(m):
    bot.send_message(m.chat.id, "0-6")


@bot.message_handler(commands=['game'])
def greet(m):
    msg_text = "ВАШ ХОД"
    coordinates = get_coordinates()
    markup = get_board(coordinates)
    bot.send_message(m.chat.id, msg_text, reply_markup=markup)


def get_board(coordinates):
    black_tile = False
    btns = []
    for row in range(8):
        for col in range(8):
            if coordinates[row][col] == 0:
                unit = pieces[0][1] if black_tile else pieces[0][0]
            else:
                unit = pieces[coordinates[row][col]]
            btns.append(types.InlineKeyboardButton(text=unit, callback_data=f'{row}-{col}'))
            black_tile = not black_tile if col < 7 else black_tile
    markup = Keyboa(items=btns, items_in_row=8).keyboard
    return markup


@bot.callback_query_handler(lambda call: True)
def btn_handler(c):
    print(c.data)


bot.polling(none_stop=True)
