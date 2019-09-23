import requests
import datetime
'''
Получить курс нескольких валют за текущую дату.

Сообщение в виде списка, вроде: «За 11.04.2019 курс 2.12 рублей за 1 Евро,
228… за 1 доллар»
http://www.nbrb.by/APIHelp/ExRates
'''


rates = requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
                     ).json()
# print(rates)
print('Курсы по состоянию на', datetime.datetime.today().date())
for rate in rates:
    if rate['Cur_Abbreviation'] in ('USD', 'RUB', 'EUR'):
        print(f"{rate['Cur_Scale']} {rate['Cur_Name']}"
              f" = {rate['Cur_OfficialRate']} белорусских рублей")
