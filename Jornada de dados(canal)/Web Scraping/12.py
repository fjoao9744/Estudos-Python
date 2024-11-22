from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import sqlite3

'''
import os
import discord
from dotenv import load_dotenv
'''

def pagina(url): 
    response = requests.get(url)

    return response.text

def filtrar_tag(html) -> dict: 
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


def create_connection(db_name='iphone_prices.db'):
    db = sqlite3.connect(db_name)
    return db

def setup_database(db):
    
    cursor = db.cursor() 

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hora_atual TEXT,
            nome TEXT,
            full REAL,
            parse REAL
        )
    ''')

    db.commit()

def save_in_db(datab, product): #recebe a tabela e adiciona o produto dentro
    new_row = pd.DataFrame([product])
    new_row.to_sql('prices', datab, if_exists='append', index=False)

def get_max_price(db):

    cursor = db.cursor()

    cursor.execute("SELECT MAX(full), hora_atual FROM prices") # pega o maior preço da tabela

    result = cursor.fetchone() # guarda o resultado da seleção em uma varaivel
    return result[0], result[1]


tabela = create_connection()
setup_database(tabela)

'''
#criação do bot de discord
intents = discord.Intents.default()  
intents.message_content = True  
intents.members = True  

client = discord.Client(intents=intents)

async def discord(message):
    
    guild_id = '1308916432012181554' #    id do servidor
    channel_id = '1308916468129202227' #    id do canal
    
    guild = client.get_guild(int(guild_id))
    if guild:
        channel = guild.get_channel(int(channel_id))
        if channel:
            await channel.send(message)

load_dotenv() # carrega as variaveis

token = os.getenv("DISCORD_SERVER_TOKEN") 

# Coloque o token do seu bot aqui
client.run(token)
'''

while True:
    page = pagina("https://produto.mercadolivre.com.br/MLB-5085319476-xiaomi-poco-c65-8gb-ram-256gb-com-nfc-global-original-_JM?attributes=COLOR_SECONDARY_COLOR%3AQXp1bC1hw6dv&quantity=1")
    product = filtrar_tag(page)

    maior_price = product["full"]
    maior_price_time = product["hora_atual"]

    atual_price, atual_price_time = get_max_price(tabela)

    if atual_price > maior_price:
        print("preço subiu")
        maior_price = atual_price
        maior_price_time = atual_price_time

    else:
        '''
        print("a")
        discord(f"maior preço : {maior_price} as {maior_price_time}")
        '''
        pass

    save_in_db(tabela, product)
    
    time.sleep(10)
