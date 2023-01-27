from keyboa import Keyboa
from telebot import TeleBot, types
from TOKEN import token
from pieces import *
from game import *

bot = TeleBot(token)
game = Game()


@bot.message_handler(commands=['start'])
def greet(m):
    bot.send_message(m.chat.id, pieces[7])


@bot.message_handler(commands=['game'])
def greet(m):
    msg_text = "ВАШ ХОД"
    markup = get_board_markup(game.board)
    bot.send_message(m.chat.id, msg_text, reply_markup=markup)


def get_board_markup(board):
    black_tile = False
    btns = []
    for row in range(8):
        for col in range(8):
            if board[row][col] == 0:
                unit = pieces[0][1] if black_tile else pieces[0][0]
            elif type(board[row][col]) == list:
                unit = pieces[board[row][col][0]]
            else:
                unit = pieces[board[row][col]]
            btns.append(types.InlineKeyboardButton(text=unit, callback_data=f'{row}-{col}'))
            black_tile = not black_tile if col < 7 else black_tile
    markup = Keyboa(items=btns, items_in_row=8).keyboard
    return markup


@bot.callback_query_handler(lambda call: True)
def btn_handler(c):
    coordinates = c.data.split('-')
    x, y = int(coordinates[0]), int(coordinates[1])
    if game.move_from(x, y) == -1:
        return
    markup = get_board_markup(game.board)
    bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, c.inline_message_id, reply_markup=markup)


bot.infinity_polling()
