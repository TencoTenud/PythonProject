import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='McFlurry', callback_data='McFlurry')],
                   [InlineKeyboardButton(text='Nugget', callback_data='Nugget')],
                   [InlineKeyboardButton(text='Coke', callback_data='Coke')],
                   [InlineKeyboardButton(text='Fries', callback_data='Fries')],
               ])
    bot.sendMessage(chat_id, 'What would you like to order?', reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    if query_data == 'McFlurry':
        bot.answerCallbackQuery(query_id, text='Sold out!')
    elif query_data == 'Nugget':
        bot.answerCallbackQuery(query_id, text='Nugget in good order')
    else:
        bot.answerCallbackQuery(query_id, text='You have ordered '+query_data)

TOKEN = '5997125741:AAH1QKwbH9vEbHddWpoku_Q6pe_RdB3Ht88'

bot = telepot.Bot(TOKEN)
MessageLoop(bot,  {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)