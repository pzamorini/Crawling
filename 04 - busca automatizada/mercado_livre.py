# Exemplo
# Obtendo produtos do Mercado Livvre a partir de uma busca realizada pelo usuário 

import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

nome_produto = input("Qual produto você deseja? ")

response = requests.get(url_base + nome_produto)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

for produto in produtos: 
  titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
  link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})

  money_symbol = produto.find('span', attrs={'class': 'andes-money-amount__currency-symbol'})
  money_fraction = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
  money_cents = produto.find('span', attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})

  # print(produto.prettify())
  print('Titulo do produto:', titulo.text)
  print('Link do produto:', link['href'])

  if money_symbol and money_fraction and money_cents:
    print('Preço do produto:', money_symbol.text + '' + money_fraction.text + ',' + money_cents.text)
  else:
    print('Preço do produto:', money_symbol.text + '' + money_fraction.text)

  print('\n\n')