import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL = "https://soware.ru/categories/reference"

res = requests.get(URL)

if not res.ok:
    raise Exception()

soup = bs(res.text, 'html.parser')

cats = soup.find_all('a', {'class': 'dqvSXx'})

res = []
for cat in cats:
    res.append((cat['href'], cat.text))

df = pd.DataFrame(res)
df.to_csv('categories.csv', decimal='\t')



print(df)