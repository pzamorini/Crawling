# Exemplo
# Obtendo produtos do Mercado Livvre a partir de uma busca realizada pelo usuário 

import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

nome_produto = input("Qual produto você deseja? ")

response = requests.get(url_base + nome_produto)

site = BeautifulSoup(response.text, 'html.parser')

produto = site.find('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

print(produto.prettify())
