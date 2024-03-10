import requests
from bs4 import BeautifulSoup

response = requests.get('http://memoria2.cnpq.br/web/guest/chamadas-publicas?p_p_id=resultadosportlet_WAR_resultadoscnpqportlet_INSTANCE_0ZaM&filtro=abertas/')

content = response.content

site = BeautifulSoup(content, 'html.parser')
# primeiro parâmetro é o conteudo, segundo é dizendo ao beautifulsoup que o conteúdo
# é em html

#print(site.prettify())

 # CHAMADAS PÚBLICAS CNPQ 

chamadas = site.findAll('div', attrs={'class': 'content'}) 
pdfs_chamadas = site.findAll('div', attrs={'class': 'links-normas pull-left'})
# tag, parâmetro {dict}

for chamada in chamadas: 
  # print(chamada.text)

  # TITULO DA CHAMADA 
  titulo = chamada.find('h4')

  # DESCRIÇÃO 
  descricao = chamada.find('p')

  #DATA 
  data = chamada.find('div', attrs={'class': 'inscricao'})

for pdf_chamada in pdfs_chamadas:
  link_edital = pdf_chamada.find('a', attrs={'class': 'btn'})

print(titulo.text + '\n' + descricao.text + '\n' + data.text
      + '\n' + f"Chamada: {link_edital['href']}")