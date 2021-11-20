import os, requests
from bs4 import BeautifulSoup

url = requests.get('https://www.adorocinema.com/filmes/filme-256880/')
html = url.content

site = BeautifulSoup(html, 'html.parser')

texto = site.find('div', attrs={'class': 'titlebar-title titlebar-title-lg'} )
texto1 = site.find('span', attrs={'class': 'ACrL2ZACrpbG1lcy9hZ2VuZGEvd2Vlay0yMDIxLTEyLTE2Lw== date blue-link'} )
texto2 = site.find('span', attrs={'class': 'ACrL2ZACrpbG1lcy10b2Rvcy9nZW5lcm8tMTMwMjUv'} )
texto3 = site.find('span', attrs={'class': 'ACrL2ZACrpbG1lcy10b2Rvcy9nZW5lcm8tMTMwMDEv'} )
texto4 = site.find('span', attrs={'class': 'ACrL2ZACrpbG1lcy10b2Rvcy9nZW5lcm8tMTMwMTIv'} )
texto5 = site.find('div', attrs={'class': 'meta-body-item meta-body-direction'} )
texto6 = site.find('div', attrs={'class': 'meta-body-item meta-body-actor'} )
texto7 = site.find('div', attrs={'class': 'content-txt'} )

if texto:
  titulo = texto.text
  print("Nome do filme: ",titulo,"\n")

  data = texto1.text
  print("Data de lançamento: ",data,"\n")

  genero1 = texto2.text
  genero2 = texto3.text
  genero3 = texto4.text
  print("Genêro: ",genero1,",",genero2,",",genero3,"\n")

  diretor = texto5.text
  print(diretor,"\n")

  elenco = texto6.text
  print(elenco,"\n")

  sinopse = texto7.text
  print("Sinopse: ",sinopse,"\n")

else:
  print("O html não foi encontrado!")

os.system("pause")