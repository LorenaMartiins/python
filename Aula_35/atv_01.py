import os, requests
from bs4 import BeautifulSoup

url = requests.get('https://www.shueisha-mteixeira.com.br/')
html = url.content

site = BeautifulSoup(html, 'html.parser')

texto = site.find('div', attrs={'id': 'feitoPor'} )

if texto:
  nome = texto.text
  print(nome.replace("Feito por ", ""))
else:
  print("O html não foi encontrado!")

os.system("pause")