import sys
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

URL = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:' \
      '%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'

URL_PARSE = urlparse(URL)
DOMEN = '{0}://{1}'.format(URL_PARSE.scheme, URL_PARSE.netloc)


def count_wiki(url, result_dict):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            div = soup.find('div', id="mw-pages")
            array_data = []
            for li in div.find_all('li'):
                array_data.append(li.find('a').contents[0][:1])
            dict_first_char = {key: array_data.count(key) for key in set(array_data)}
            for key in dict_first_char:
                try:
                    result_dict[key] += dict_first_char[key]
                except KeyError:
                    result_dict[key] = dict_first_char[key]
            try:
                next_page = div.find_all(
                    'a',
                    title='Категория:Животные по алфавиту',
                    text='Следующая страница'
                )[-1].get('href')
                next_link = '{}{}'.format(DOMEN, next_page)
                count_wiki(next_link, result_dict)
            except IndexError:
                return result_dict
    except requests.exceptions.ConnectionError:
        print('Ошибка загрузки')
        sys.exit()


def main():
    result = dict()
    count_wiki(URL, result)
    for key in sorted(result):
        print('{0}: {1}'.format(key, result[key]))


if __name__ == '__main__':
    main()
