import requests
from bs4 import BeautifulSoup as bs

URL = "https://soware.ru/categories/clients-and-partners-search-services"

res = requests.get(URL)

if not res.ok:
    raise Exception()

soup = bs(res.text, 'html.parser')

links = soup.find_all('a', {'class': 'dEWdHg'})
res = []
tests = soup.select('a ~ small') #{'class': 'dEWdHg'})

# test.text

for link, test in zip(links, tests):
    res.append((link['href'], test.text))



print(res)