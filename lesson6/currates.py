import requests
import datetime
'''
Получить курс нескольких валют за текущую дату.

Сообщение в виде списка, вроде: «За 11.04.2019 курс 2.12 рублей за 1 Евро,
228… за 1 доллар»
http://www.nbrb.by/APIHelp/ExRates
'''

def rate(currency, date_value=None):
    try:
        if date_value is None:
            request_rate = requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0')
        else:
            input_date = date_value.isoformat()
            request_rate = requests.get(
                f'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0&onDate={input_date}')
    except ConnectionError:
        return "Couldn't connect to NBRB"
    if request_rate.status_code == 200:
        rates = request_rate.json()
        dict_rates = {rate['Cur_Abbreviation']: (
            rate['Cur_Scale'],
            rate['Cur_Name'],
            rate['Cur_OfficialRate']
            ) for rate in rates}
        return dict_rates[currency.upper()]
    return request_rate.status_code

if __name__ == '__main__':
    print(rate('eur'))
    # print('Курсы по состоянию на', datetime.datetime.today().date())
    # for rate in rates:
    #     if rate['Cur_Abbreviation'] in ('USD', 'RUB', 'EUR'):
    #         print(f"{rate['Cur_Scale']} {rate['Cur_Name']}"
    #             f" = {rate['Cur_OfficialRate']} белорусских рублей")
