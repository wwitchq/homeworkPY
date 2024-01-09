"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""
import requests
from bs4 import BeautifulSoup

ya_chart_page = requests.get(url='https://music.yandex.ru/chart')
ya_page_html = 'chart.html'

data = {}
# Если html файл скачан успешно, то не раскоменчиваем
# with open(ya_page_html,'wb') as fl:
#     fl.write(ya_chart_page.content)

with open(ya_page_html, 'r', encoding='utf-8') as fl:  # r - read, encoding = utf-8 позволяет читать русские буквы
    soup = BeautifulSoup(fl.read(), 'lxml')
    all_tracks: list[BeautifulSoup] = soup.find_all("div", class_="d-track")
    for pos, track in enumerate(all_tracks):
        title = track.find('div', class_='d-track__name').text.strip().replace('    ', '').replace('\n', ' ')
        author = track.find('div', class_='d-track__meta').text.strip().replace(' ', '').replace('\n', ' ')
        time = track.find('span', class_='typo-track').text
        data[pos + 1] = (title, author, time)

import json

with open('data.json', 'w') as fl:  # w - write
    json.dump(data, fl, ensure_ascii=False)