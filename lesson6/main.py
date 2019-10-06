from class_bot import MoneyBot
from token_auth import token
from utils import logg_this

test_bot = MoneyBot(token)
money = test_bot.get_money()
answer = test_bot.get_message()
chat_id = answer['chat_id']
text = answer['text']
logg_this(answer)

if text == '/course':
    test_bot.send_message(chat_id, money)

recorder = test_bot.record_message_file()
