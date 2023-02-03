from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re
from datetime import datetime
startTime = datetime.now()

print('Iniciado')

#Convertendo avaliacao
def avaliacao_conv(a):
        if a == 'One':
            a = 1
        elif a == 'Two':
            a = 2
        elif a == 'Three':
            a = 3
        elif a == 'Four':
            a = 4
        elif a == 'Five':
            a = 5
        else:
            a = 0

        return a


## Fazendo o Web Scrapping dos dados dos livros ##

'Video usado para aprender web scrapping'
link_video1 =  "https://www.youtube.com/watch?v=RvCBzhhydNk"


url = 'https://books.toscrape.com/catalogue/page-1.html'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

'Acha o numero de paginas'
num_pagina = int(str(soup.find('li', class_ = 'current' ).text).\
        replace('\n','').replace(' ', '').\
        split('of')[1])

'Fazendo a busca pelos livros'

df = []

# for i in range(num_pagina):
for pagina in range(num_pagina):
    url = f'https://books.toscrape.com/catalogue/page-{pagina+1}.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    'Procurando livros dentro da pagina'
    lists = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3' )
    for i in lists:
        'Buscando o titulo do livro'
        titulo = str(i.find('h3'))
        titulo = titulo.split('=')[1].split(' ')[0].replace('"', '')
        # print(titulo)
        # print('------------------------')

        new_url = 'https://books.toscrape.com/catalogue/' + titulo
        page_book = requests.get(new_url)
        soup_book = BeautifulSoup(page_book.content, 'html.parser')

        'Nome do livro'
        nome = soup_book.find('h1').text
        # print(nome)

        'Valor do livro'
        valor = soup_book.find('p', class_ = 'price_color').text
        # print(valor)

        'Avaliação do Livro'
        avaliacao = str(soup_book.find_all('p')).split('<')[7].split(' ')[2].replace('">', '').replace('\n', '').replace(' ','')
        avaliacao = avaliacao_conv(avaliacao)
        # print(avaliacao)

        'Se esta em Estoque'
        estoque = str(list(soup_book.find_all('td'))[5]).replace('<td>', '').replace('</td>', '')
        # print(estoque)
        
        'Categoria do livro'
        categorias = soup_book.find_all('ul', class_ = 'breadcrumb')
        for categoria in categorias:
            cate = str(list(categoria.find_all('a'))[2]).split('">')[1].split('<')[0]
        # print(cate)


        'Descrição do livro'

        descricao = list(soup_book.find_all('p'))[3].text
        # print(descricao)
        
        df.append([nome, valor, avaliacao, estoque, cate, descricao])

df = pd.DataFrame(df)

df.to_csv('Dados_livros.csv', index = False, sep=';')
print(df)
print(datetime.now() - startTime)


    