from class_bot import Bot
import datetime
import requests
from bs4 import BeautifulSoup
from http.client import responses


class RateBot(Bot):
    def __init__(self, token):
        super().__init__(token)
        self.rate_url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
        self.habr_url = "https://habr.com/top/monthly/"
        # self.habr_html = requests.get(self.habr_url).text
        self._last_status = 0
        
    @property
    def last_status(self):
        return self._last_status
    
    def habr_html(self):
        r = requests.get(self.habr_url)
        self._last_status = r.status_code
        if r.status_code == 200:
            return r.text
        return r.status_code + " " + responses[r.status_code]

    def _rate_get_date(self, day_=None, month_=None, year_=None):
        if day_ is None and month_ is None and year_ is None:
            return self.rate_url
        in_date = self.date_to_iso(day_, month_, year_)
        add_url = f"&onDate={in_date}"
        return self.rate_url + add_url

    def date_to_iso(self, day_, month_, year_):
        return datetime.date(year_, month_, day_).isoformat()

    def rate(self, currency, day_=None, month_=None, year_=None):
        request_rate = requests.get(self._rate_get_date(day_, month_, year_))
        self._last_status = request_rate.status_code
        if request_rate.status_code == 200:
            rates = request_rate.json()
            dict_rates = {rate['Cur_Abbreviation']: (
                rate['Cur_Scale'],
                rate['Cur_Name'],
                rate['Cur_OfficialRate']
                ) for rate in rates}
            return dict_rates[currency.upper()]
        return request_rate.status_code + " " + responses[request_rate.status_code]

    def _get_data(self):
        soup = BeautifulSoup(self.habr_html, 'lxml')
        for h2 in soup.find_all('article'):
            yield h2.find('h2').a.text

    def _get_all_data(self):
        soup = BeautifulSoup(self.habr_html(), 'lxml')
        return [block.find('h2').a.text for block in soup.find_all('article')]

    def habr(self, num=None):
        texts = self._get_all_data()
        if num is None:
            return texts
        if len(texts) >= num:
            return texts[num - 1]
        return "Sorry! We don't have so many articles from habr"
