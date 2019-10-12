import requests
import time

cur_time = time.asctime()


class Bot:
    def __init__(self, token):
        self.token = token
        self.url = f'https://api.telegram.org/bot{self.token}/'
        self.last_updates = 0

    def get_updates(self):
        method = 'getUpdates'
        req = requests.get(self.url + method)
        return req.json()

    def get_message(self):
        data = self.get_updates()
        cur_update = data['result'][-1]['update_id']
        if cur_update == self.last_updates:
            return None
        last_message = data['result'][-1]['message']
        chat_id = last_message['chat']['id']
        text = last_message['text']
        message = {
            'chat_id': chat_id,
            'text': text,
        }
        self.last_updates = cur_update
        return message

    def send_message(self, chat_id, text):
        method = 'sendMessage'
        params = {
            'chat_id': chat_id,
            'text': text,
        }
        response = requests.post(self.url + method, params)
        return response
    
    def get_user_messages(self, chat_id):
        data = self.get_updates()
        messages = data['result']
        chat_messages = list(filter(self._filter_chat_id(chat_id), messages))
        return chat_messages
    
    def get_user_message(self, chat_id, num):
        messages = self.get_user_messages(chat_id)
        if num > len(messages) - 1:
            return None
        return messages[-num - 1]['message']['text']
    
    def _filter_chat_id(self, chat_id):
        cur_chat_id = chat_id
        def filt(result):
            return result['message']['chat']['id'] == cur_chat_id
        return filt


class MoneyBot(Bot):
    def __init__(self, token):
        super().__init__(token)
        self.money_url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'

    def get_money(self):
        response = requests.get(self.money_url).json()
        usd_price = eur_price = pln_price = 'NOT_FOUND'
        for p in list(response):
            if p['Cur_Abbreviation'] == 'USD':
                usd_price = p['Cur_OfficialRate']
            if p['Cur_Abbreviation'] == 'EUR':
                eur_price = p['Cur_OfficialRate']
            if p['Cur_Abbreviation'] == 'PLN':
                pln_price = p['Cur_OfficialRate']
        return f'Cost of one BYN today - {usd_price} USD, {eur_price} EUR, {pln_price} PLN'

    def record_message_file(self):
        with open('messages/message' + cur_time + '.txt', 'w') as message_file:
            last_user_message = self.get_updates()['result'][-1]['message']['text']
            message_file.write(last_user_message + '\n')
