import time
import telepot
import json
from telepot.loop import MessageLoop
from telepot.delegate import pave_event_space, per_chat_id, create_open
from telepot.namedtuple import ReplyKeyboardMarkup

class GoldenArches(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(GoldenArches, self).__init__(*args, **kwargs)
        self.indicator = 'choose_order'
        self.order = {}

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if self.indicator == 'choose_order':
            mark_up = ReplyKeyboardMarkup(keyboard=[['McFlurry'], ['Nugget'], ['Coke'], ['Fries']],
                                          one_time_keyboard=True)
            bot.sendMessage(chat_id, text='What would you like to order?', reply_markup=mark_up)
            self.indicator = 'choose_payment'
        elif self.indicator == 'choose_payment':
            self.order['order'] = msg['text']
            mark_up = ReplyKeyboardMarkup(keyboard=[['Cash'], ['CeditCard']],
                                          one_time_keyboard=True)
            bot.sendMessage(chat_id, text='How would you like to pay?', reply_markup=mark_up)
            self.indicator = 'set_order'
        elif self.indicator == 'set_order':
            self.order['payment'] = msg['text']
            with open('order.json', 'a') as handle:
                json.dump(self.order, handle)
                handle.write("\n")
                handle.close()
            bot.sendMessage(chat_id, 'Order Accepted: Order ' + self.order['order'] + ' payment ' + self.order['payment'])


TOKEN = '5997125741:AAH1QKwbH9vEbHddWpoku_Q6pe_RdB3Ht88'

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, GoldenArches, timeout=5),
])
MessageLoop(bot).run_as_thread()

while 1:
    time.sleep(10)