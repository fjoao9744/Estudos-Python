import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import sqlite3

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

def save_in_df(product, df): # a funçao vai receber o produto a ser salvo dentro de um dataframe e a dataframe
    new_row = pd.DataFrame([product]) # linha que vai ser armazenada dentro do dataframe
    df = pd.concat([df, new_row], ignore_index=True) # df vai ser o dataframe passado com a nova linha
    return df

def create_connection(db_name='iphone_prices.db'): # essa função cria um banco de dados local
    db = sqlite3.connect(db_name) # cria a tabela que vai ser o banco de dados local
    return db

def setup_database(db): # cria a tabela se ela não existir
    
    cursor = db.cursor() 

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hora_atual TEXT,
            name TEXT,
            full INTEGER,
            parse INTEGER
        )
    ''')
    db.commit()

df = pd.DataFrame() # cria uma tabela vazia
while True:
    page = pagina("https://produto.mercadolivre.com.br/MLB-5085319476-xiaomi-poco-c65-8gb-ram-256gb-com-nfc-global-original-_JM?attributes=COLOR_SECONDARY_COLOR%3AQXp1bC1hw6dv&quantity=1")
    product = filtrar_tag(page)

    df = save_in_df(product, df)
    
    time.sleep(0.5)

    print(df)