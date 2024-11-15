import requests
from bs4 import BeautifulSoup

def pagina(url): 
    response = requests.get(url)

    return response.text

def filtrar_tag(html): 
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find("h1", class_="ui-pdp-title").get_text()
    prices = soup.find_all("span", class_="andes-money-amount__fraction")
    
    full_price = float(prices[0].get_text())
    parse_price = float(prices[1].get_text())

    print(full_price, parse_price)

page = pagina("https://produto.mercadolivre.com.br/MLB-5085319476-xiaomi-poco-c65-8gb-ram-256gb-com-nfc-global-original-_JM?attributes=COLOR_SECONDARY_COLOR%3AQXp1bC1hw6dv&quantity=1")

filtrar_tag(page)

