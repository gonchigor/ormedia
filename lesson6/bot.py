import requests
import json
from time import sleep
from token_auth import token
from currates import rate
from datetime import date
from habr import get_habr

last_updates = 0
URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    if len(data['result']):
        chat_id = data['result'][-1]['message']['chat']['id']
        global last_updates
        cur_update = data['result'][-1]['update_id']
        if last_updates != cur_update:
            last_updates = cur_update
            message_text = data['result'][-1]['message']['text']
            message = {'chat_id': chat_id, 'text': message_text}
            return message
    return None


def send_message(chat_id, text):
    try:
        url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
        r = requests.get(url)
        if r.status_code == 200:
            return True
        return False
    except Exception:
        return False


def main():
    #     d = get_updates()
    #     with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)
    # print(get_message())
    try:
        while True:
            answer = get_message()
            if answer is not None:
                chat_id = answer['chat_id']
                answer_text = answer['text']
                answer_text_words = answer_text.split()
                if 'ничего' in answer['text']:
                    send_message(chat_id, 'Тогда проваливай')
                elif len(answer_text_words):
                    if answer_text_words[0].upper() in ('/USD', '/EUR', '/RUB'):
                        try:
                            if len(answer_text_words) == 1:
                                send_message(chat_id,
                                             'Курс {} {} на сегодня: {}'.format(
                                                *rate(answer_text_words[0][1:])))
                            else:
                                date_value = date(int(answer_text_words[3]),
                                                  int(answer_text_words[2]),
                                                  int(answer_text_words[1]))
                                send_message(chat_id,
                                             'Курс {1} {2} на {0}: {3}'.format(
                                                date_value.isoformat(),
                                                *rate(answer_text_words[0][1:],
                                                      date_value)
                                             ))
                        except (KeyError, ValueError):
                            send_message(chat_id, 'Something wrong!!!')
                        except Exception as e:
                            print(type(e))
                            send_message(chat_id, "Incorrect command")
                    elif answer_text_words[0].upper() == '/HABR':
                        if len(answer_text_words) == 1:
                                messages = get_habr()
                                for mes in messages:
                                    send_message(chat_id, mes)
                        else:
                            send_message(chat_id, get_habr(
                                int(answer_text_words[1])
                            ))
                    else:
                        send_message(chat_id, 'Что тебе нужно?')
                else:
                    send_message(chat_id, 'Not understand')
            sleep(3)
    except KeyError:
        print("Invalid token")

if __name__ == '__main__':
    main()
