import os, requests
from bs4 import BeautifulSoup

url = requests.get('https://www.shueisha-mteixeira.com.br/')
html = url.content

site = BeautifulSoup(html, 'html.parser')

texto = site.find('div', attrs={'class': 'titulo'})

if texto:
  #print(texto.prettify())
  print(texto.text)
else:
  print("O html não foi encontrado!")

os.system("pause")