from ratebot import RateBot
from token_auth import token
from time import sleep
import logging
import time

rateBot = RateBot(token)
cur_time = time.asctime()
logging.basicConfig(filename='logs/log' + str(cur_time) + '.log',
                        level=logging.INFO, filemode='w')

while True:
    try:
        answer = rateBot.get_message()
        if answer is not None:
            chat_id = answer['chat_id']
            answer_text = answer['text']
            answer_text_words = answer_text.split()
            if 'ничего' in answer_text:
                rateBot.send_message(chat_id, 'Тогда проваливай')
            elif len(answer_text_words):
                if answer_text_words[0].upper() in ('/USD', '/EUR', '/RUB'):
                    if len(answer_text_words) == 1:
                        rateBot.send_message(chat_id, 'Курс {} {} на сегодня: {}'.format(
                                        *rateBot.rate(answer_text_words[0][1:])))
                    else:
                        day = int(answer_text_words[1])
                        month = int(answer_text_words[2])
                        year = int(answer_text_words[3])
                        dateiso = rateBot.date_to_iso(day, month, year)
                        rateBot.send_message(chat_id,
                                'Курс {1} {2} на {0}: {3}'.format(dateiso,
                                *rateBot.rate(answer_text_words[0][1:],
                                              day, month, year)))
                elif answer_text_words[0].upper() == '/HABR':
                    if len(answer_text_words) == 1:
                            messages = rateBot.habr()
                            for mes in messages:
                                rateBot.send_message(chat_id, mes)
                    else:
                        rateBot.send_message(chat_id, rateBot.habr(
                            int(answer_text_words[1])
                        ))
        else:
            sleep(2)
    except Exception as e:
        logging.error(type(e))
