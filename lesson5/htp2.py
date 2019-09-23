import requests
from bs4 import BeautifulSoup
'''
Получить список статей хабра за месяц.
https://habr.com/top/monthly/
'''


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    for h2 in soup.find_all('article'):
        yield h2.find('h2').a.text


def main():
    page = get_html('https://habr.com/top/monthly/')
    for top_header in get_data(page):
        print(top_header)


if __name__ == '__main__':
    main()
