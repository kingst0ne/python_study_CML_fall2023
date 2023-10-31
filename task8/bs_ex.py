import requests
from bs4 import BeautifulSoup as bs

URL = "https://soware.ru"

res = requests.get(URL)

if not res.ok:
    raise Exception()

soup = bs(res.text, 'html.parser')

soup.find_all('div')

soup.find_all('div', {'class': 'class_name', 'id':'name_id'})


soup.find('div')

soup.find('qwertyuio')

soup.select('div')
soup.select_one('div')

soup.select('div.class_name')
soup.select('.class_name')

soup.select('div#id_name')
soup.select('#id_name')

soup.select('[href]')
soup.select('[href = "http://..."]')

soup.select('div a')
soup.select('div div p')

soup.select('div > a')
soup.select('div > div > a')

soup.select('h1 ~ span')

h1 = soup.h1

h1_ = soup.h1.a

p = soup.div.p[0]