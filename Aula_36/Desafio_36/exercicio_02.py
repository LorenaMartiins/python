# Programa 2 que monta uma planilha com informações extraídas de uma página web 

import os, requests, openpyxl
from bs4 import BeautifulSoup
from openpyxl.styles import Border, Side, Alignment

n_filmes = int(input("Digite aqui quantos filmes vc quer colocar na planilha: "))

planilha = openpyxl.Workbook()

page = planilha['Sheet']
page.title = 'filmes'

estilo = Side(border_style='thin', color='000000')
borda = Border(top=estilo, bottom=estilo, left=estilo, right=estilo)

page.append(['TITULO', 'DATA DE LANÇAMENTO', 'DIRETOR', 'ELENCO'])

for x in range(n_filmes):
  url4 = requests.get(input("Digite aqui a url de um filme ou serie do site adorocinema: "))
  html4 = url4.content
  film1 = BeautifulSoup(html4, 'html.parser')

  titulo = film1.find('div', attrs={'class': 'titlebar-title titlebar-title-lg'} )
  data_um = film1.find('div', attrs={'class': 'meta-body-item meta-body-info'} )
  genero_um = film1.find('div', attrs={'class': 'meta-body-item meta-body-info'} )
  diretor = film1.find('div', attrs={'class': 'meta-body-item meta-body-direction'} )
  elenco = film1.find('div', attrs={'class': 'meta-body-item meta-body-actor'} )

  data_um = data_um.find('span')
  dataresp = data_um.text
  titulo = titulo.text
  diresp = diretor.text
  elenco = elenco.text

  page.append([ titulo, dataresp, diresp, elenco ])

for y in range(1,2):
  page['A'+str(y)].alignment = Alignment(horizontal='center')
  page['B'+str(y)].alignment = Alignment(horizontal='center')
  page['C'+str(y)].alignment = Alignment(horizontal='center')
  page['D'+str(y)].alignment = Alignment(horizontal='center')

for z in range(1,2):
  page['A'+str(z)].border = borda
  page['B'+str(z)].border = borda
  page['C'+str(z)].border = borda
  page['D'+str(z)].border = borda

page.column_dimensions['A'].width = 45
page.column_dimensions['B'].width = 23
page.column_dimensions['C'].width = 35
page.column_dimensions['D'].width = 55

planilha.save('filmes.xlsx')

os.system("pause")