from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
from os import path
import requests
from urllib.parse import urljoin
import tabula

html = 'http://www.saude.pr.gov.br/modules/conteudo/conteudo.php?conteudo=3507'
response = requests.get(html)
bs = BeautifulSoup(response.text, 'html.parser')

for link in bs.find('div', {'id' : 'page'}).find_all('a'): 
        arquivo = os.path.join(link['href'].split('/')[-1])
        print(arquivo)
        with open(arquivo, 'wb') as pdf:
                pdf.write(requests.get(urljoin(html,link['href'])).content)
       

