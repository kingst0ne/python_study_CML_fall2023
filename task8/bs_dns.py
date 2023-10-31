import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#
# URL = "https://dns-shop.ru/catalog/0985b00c0516c6ed/elektronnaya-cifrovaya-podpis/"
#
# res = requests.get(URL)
#
# if not res.ok:
#     raise Exception()


with open('index.html',encoding='utf-8') as fp:
    soup = bs(fp, 'html.parser')


names = soup.find_all('a', {'class': 'catalog-product__name'})

id_list = soup.select('div.catalog-product')


res = []
for name,_id in zip(names, id_list):
    res.append((_id['data-code'], name['href'], name.text))

df = pd.DataFrame(res)
df.to_csv('dns.csv', decimal='\t')

pass

#<div data-id="product" class="catalog-product ui-button-widget " data-product="dafa3c30-1440-11ec-8ee7-00155d8ed20b" data-code="4866657" data-preview-slider-inited="1"><div class="catalog-product__image"><a class="catalog-product__image-link" href="/product/dafa3c301440ed20/usb-token-jacarta-lt-sertifikat-fstek/" data-toggle-slider=""><picture><source type="image/webp" media="(min-width: 768px)" data-srcset="https://c.dns-shop.ru/thumb/st4/fit/200/200/d186685504b457d10eace24f82114bc7/cc8fe28b2de2f9690735b71159a6f7aeb9eb1afc186057d42465a5815ac41a8d.jpg.webp" srcset="https://c.dns-shop.ru/thumb/st4/fit/200/200/d186685504b457d10eace24f82114bc7/cc8fe28b2de2f9690735b71159a6f7aeb9eb1afc186057d42465a5815ac41a8d.jpg.webp"><source type="image/webp" media="(max-width: 767px)" data-srcset="https://c.dns-shop.ru/thumb/st4/fit/120/120/e040d2615235b96bb7b6b31851a88af7/cc8fe28b2de2f9690735b71159a6f7aeb9eb1afc186057d42465a5815ac41a8d.jpg.webp" srcset="https://c.dns-shop.ru/thumb/st4/fit/120/120/e040d2615235b96bb7b6b31851a88af7/cc8fe28b2de2f9690735b71159a6f7aeb9eb1afc186057d42465a5815ac41a8d.jpg.webp"><img width="2000" height="2000" alt="USB-токен JaCarta LT Сертификат ФСТЭК" data-src="https://c.dns-shop.ru/thumb/st4/fit/200/200/d186685504b457d10eace24f82114bc7/cc8fe28b2de2f9690735b71159a6f7aeb9eb1afc186057d42465a5815ac41a8d.jpg" class="loaded" src="https://c.dns-shop.ru/thumb/st4/fit/200/200/d186685504b457d10eace24f82114bc7/cc8fe28b2de2f9690735b71159a6f7aeb9eb1afc186057d42465a5815ac41a8d.jpg" data-was-processed="true"></picture></a><span id="as-_-CIZj"></span></div><a class="catalog-product__name ui-link ui-link_black" href="/product/dafa3c301440ed20/usb-token-jacarta-lt-sertifikat-fstek/"><span>USB-токен JaCarta LT Сертификат ФСТЭК [защита персональных данных, подходит для ФНС]</span></a><div class="catalog-product__voblers"><span id="as-_OciHV"></span></div><div class="catalog-product__stat"><span class="compare-checkbox"><label class="ui-checkbox"><span>Сравнить</span><input type="checkbox" class="ui-checkbox__input"><span class="ui-checkbox__box"></span></label></span><a class="catalog-product__rating" href="/product/dafa3c301440ed20/usb-token-jacarta-lt-sertifikat-fstek/opinion/" data-rating="4.5"><i></i><i></i><i></i><i></i><i></i>495</a><a class="catalog-product__comment" href="/product/dafa3c301440ed20/usb-token-jacarta-lt-sertifikat-fstek/communicator/"><i class="catalog-product__comment-icon"></i>&nbsp;2</a><a class="catalog-product__service-rating" href="/product/dafa3c301440ed20/usb-token-jacarta-lt-sertifikat-fstek/service-rating/"><i class="catalog-product__service-rating-icon catalog-product__service-rating-icon_high"></i>Отличная надежность</a></div><span id="as-8yGGTA" class="catalog-product__buy product-buy"></span><span id="as-j3ecUS" class="catalog-product__avails avails-container"></span></div>