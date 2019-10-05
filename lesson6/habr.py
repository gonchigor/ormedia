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


def get_all_data(html):
    soup = BeautifulSoup(html, 'lxml')
    return [block.find('h2').a.text for block in soup.find_all('article')]


def main():
    page = get_html('https://habr.com/top/monthly/')
    texts = get_all_data(page)
    print(len(texts))
    print(get_habr(1))
    print(get_habr(20))
    print(get_habr(21))
        
        
def get_habr(num=None):
    page = get_html('https://habr.com/top/monthly/')
    texts = get_all_data(page)
    if num is None:
        return texts
    if len(texts) >= num:
        return texts[num - 1]
    return "Sorry! We don't have so many articles from habr"


if __name__ == '__main__':
    main()
