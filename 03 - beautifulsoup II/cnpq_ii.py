import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_chamadas = []

response = requests.get('http://memoria2.cnpq.br/web/guest/chamadas-publicas?p_p_id=resultadosportlet_WAR_resultadoscnpqportlet_INSTANCE_0ZaM&filtro=abertas/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# CHAMADAS PÚBLICAS CNPQ 
chamadas = site.findAll('div', attrs={'class': 'content'}) 
pdfs_chamadas = site.findAll('div', attrs={'class': 'links-normas pull-left'})

for chamada, pdf_chamada in zip(chamadas, pdfs_chamadas):
    titulo = chamada.find('h4')
    descricao = chamada.find('p')
    data = chamada.find('div', attrs={'class': 'inscricao'})
    link_edital = pdf_chamada.find('a', attrs={'class': 'btn'})

    #if titulo and descricao and data and link_edital:
        #print(f"Título: {titulo.text}\nDescrição: {descricao.text}\nData: {data.text}\nLink do PDF: {link_edital['href']}\n")
    lista_chamadas.append([titulo.text, descricao.text, data.text, link_edital['href']])
# a função zip serve para iterar simultaneamente sobre as listas de chamada
# e links de PDFs. Isso permite que você acesse os elementos correspondentes de 
# ambas as listas na mesma iteração.
    
chamadas_publicas = pd.DataFrame(lista_chamadas, columns=['Titulo', 'Descrição', 'Data', 'Edital'])

chamadas_publicas.to_csv('chamadas.csv', index=False)