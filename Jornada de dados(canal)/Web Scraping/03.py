import requests
from bs4 import BeautifulSoup

def pagina(url): # essa função retorna a pagina HTML mas em forma de texto
    response = requests.get(url)

    return response.text

def filtrar_tag(html): # essa função pega a tag que desejar de uma pagina html
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find("h1", class_="ui-pdp-title").get_text()
    print(name)
    prices = ...

page = pagina("https://www.mercadolivre.com.br/samsung-galaxy-m55-5g-dual-sim-256-gb-verde-claro-8-gb-ram/p/MLB36208240?pdp_filters=deal%3AMLB779362-1#polycard_client=homes-korribanSearchTodayPromotions&wid=MLB5114034720&sid=search&searchVariation=MLB36208240&position=2&search_layout=grid&type=product&tracking_id=59b6efd6-fc23-451f-acdc-57e69c30f112&c_id=/home/today-promotions-recommendations/element&c_uid=6f67736f-b80d-4bf6-899f-3c24261f424b")

filtrar_tag(page)

