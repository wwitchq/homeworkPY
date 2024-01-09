import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep
import json



cookies = {
    'PHPSESSID': 'l0jo0motfukb418bcjf7s9a8i0',
    '51a55dae53577255b792d39bfe1d40ac': '0',
    '_ga_BB3QC8QLF4': 'GS1.1.1698057575.1.1.1698059035.0.0.0',
    '_ga': 'GA1.1.887196952.1698057575',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Alt-Used': 'zaka-zaka.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=l0jo0motfukb418bcjf7s9a8i0; 51a55dae53577255b792d39bfe1d40ac=0; _ga_BB3QC8QLF4=GS1.1.1698057575.1.1.1698059035.0.0.0; _ga=GA1.1.887196952.1698057575',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}

response = requests.get('https://zaka-zaka.com/game/new', cookies=cookies, headers=headers)
}

result = {}
for i in range(1,24):
    params = {
        'p' : i,
    }


response = requests.get('https://zaka-zaka.com/game/new', cookies=cookies, headers=headers)
with open("Bish Bash Bot.html", "w", encoding="utf-8") as f:
    f.write(response.text)
with open("Bish Bash Bot.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file.read(), "lxml"):
    cards = soup.find("div",class_="game-block-name").text:
for card in cards:
   name = cards.find("div",class_="game-block-name").text.strip()
   price = cards.find("div",class_="game-block-prices").text.strip()[0:7]

print(result)

