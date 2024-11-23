## Como funciona a internet
a maioria das paginas funcionam com cliente e servidor
a gente entra em um link, requerimos das informações de um servidor, como um HTML com CSS, JS, etc
e o nosso navegador renderiza essas informações

# 01 Criar e ativar o ambiente virtual
é só digitarmos "python -m venv "nome da venv"" para criar um ambiente virtual e dai é só ir instalando as bibliotecas
agora para ativar o ambiente virtual colocamos "source "nome da venv"/Scripts/activate""

e a primeira biblioteca que vamos baixar vai ser o requests

# 02 Usando o requests
o requests é muito simples de usar, só importar, criar uma variavel com o link como string e pegamos oque esta no link com o metodo 
get("url")
lembrando que estamos trabalhando com requisições de html

se colocarmos .text na frente do response no print, ele retorna todo o texto daquele html

# 03 Pegando elementos pelas tags
não queremos trabalhar com todos os textos do site, então pegamos apenas oque nos interesa
para isso vamos no inspecionar do google e procuramos a tag que desejamos pegar, com essa tag em mãos, podemos clicar com o botão direito em cima da tag, ir em copy -> selector e copiar o caminho daquela tag

# 04 Beautiful Soup
Beautiful soup é uma biblioteca que faz justamente o trabalho de pegar oque tem dentro dentro das tags para podermos trabalhar em cima

(pip install beautifulsoup4)
from bs4 import BeautifulSoup

esse BeautifulSoup(função) serve para identificarmos sobre qual é o HTML que vamos analisar
ele recebe dois parametros, qual html que vamos usar o parser(no caso do html, 'html.parser')

agora para procurarmos por uma classe, vamos la no inspecionar ver a tag e a classe que vamos pegar e colocamos o objeto soup com o .find
dentro do .find colocamos como argumento a tag('h1') e a classe do objeto(class_="classe")
e ja que queremos pegar apenas o texto, então colocamos no final: get_text()
no final assim: 

soup = BeautifulSoup(html, 'html.parser')
name = soup.find("h1", class_="ui-pdp-title").get_text()

# 05 find_all
quando temos uma tag com mais de uma classe e queremos pegar todas as tags com aquela classe, usamos o find_all

prices = soup.find_all("span", class_="andes-money-amount__fraction")

# 06 Como pegar os preços
quando você usa o find_all você recebe uma lista de preços e para trabalhar com os preços dessa lista você tem que converter elas para um numero
mas se converter para numero vai dar um erro pq estamos tentando transformar uma tag em um numero, então usamos o get_text() na tag e depois convertemos para numero
então deve ficar assim:

prices = soup.find_all("span", class_="andes-money-amount__fraction")

full_price = float(prices[0].get_text())
parse_price = float(prices[1].get_text())

# 07 strftime
strftime é uma função da biblioteca time para pegar a hora atual e formatar como uma string

# 08 Usando o Pandas
## DataFrames
dataframes são formas de representar tabelas ao invez de usar dicionarios e utilizamos chamando a função DataFrame e colocando o dicioario a virar um dataframe

## concat
a função concat do pandas, junta duas tabelas e é simples, colocamos a primeira tabela e a segunda como argumentos e pronto

# 09 SQLite3
## connect
quando chamamos a função connect("nome do banco de dados") criamos um banco de dados local

## cursor
a função cursor possibilita a gente de manipular as informações do banco de dados 

## execute
o execute permite que usemos comandos em SQL dentro do codigo de python

## commit
salva as alterações no banco de dados que foi alterado com o execute

obs: as funções, cursor, execute e commit só funcionam se estiverem interligadas, ou seja, não tem como usar o commit ou o execute sem o cursor

1:26:00
https://www.youtube.com/watch?v=LDki9Xaw674