import requests
from bs4 import BeautifulSoup
import time

def pagina(url): 
    response = requests.get(url)

    return response.text

def filtrar_tag(html): 
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find("h1", class_="ui-pdp-title").get_text()
    prices = soup.find_all("span", class_="andes-money-amount__fraction")
    
    full_price = float(prices[0].get_text().replace(".", ''))
    try:
        parse_price = float(prices[1].get_text().replace(".", ''))
    except:
        parse_price = None

    hora = time.strftime("%Y:%m:%d %H:%M:%S") # pegando a hora atual

    return {
        "hora_atual": hora,
        "nome": name,
        "full": full_price,
        "parse": parse_price
    }


while True:
    page = pagina("https://produto.mercadolivre.com.br/MLB-5085319476-xiaomi-poco-c65-8gb-ram-256gb-com-nfc-global-original-_JM?attributes=COLOR_SECONDARY_COLOR%3AQXp1bC1hw6dv&quantity=1")
    product = filtrar_tag(page)
    print(product)
    time.sleep(0.5)