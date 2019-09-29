import requests
import json
from time import sleep
from token import token

last_updates = 0
URL = 'https://api.telegram.org/bot' + token + '/'

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()
    
def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    global last_updates
    cur_update = data['result'][-1]['update_id']
    if last_updates != cur_update:
        last_updates = cur_update
        message_text = data['result'][-1]['message']['text']
        message = {'chat_id': chat_id,
                'text': message_text}
        return message
    return None


def send_message(chat_id, text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():
#     d = get_updates()
#     with open('updates.json', 'w') as file:
#         json.dump(d, file, indent=2, ensure_ascii=False)
    # print(get_message())
    answer = get_message()
    chat_id = answer['chat_id']
    if 'ничего' in answer['text']:
        send_message(chat_id, 'Тогда проваливай')
    else:
        send_message(chat_id, 'Что тебе нужно?')

if __name__ == '__main__':
    main()
