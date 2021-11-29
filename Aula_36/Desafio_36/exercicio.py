# Programa que monta uma planilha com informações extraídas de uma página web.

import os, requests, openpyxl
from bs4 import BeautifulSoup
from openpyxl.styles import Border, Side, Alignment

url1 = requests.get('https://www.ibge.gov.br/cidades-e-estados/sp/ribeirao-preto.html')
url2 = requests.get('https://www.ibge.gov.br/cidades-e-estados/sp/sao-paulo.html')
url3 = requests.get('https://www.ibge.gov.br/cidades-e-estados/sp/barrinha.html')

html1 = url1.content
html2 = url2.content
html3 = url3.content

city1 = BeautifulSoup(html1, 'html.parser')
city2 = BeautifulSoup(html2, 'html.parser')
city3 = BeautifulSoup(html3, 'html.parser')

rib = city1.find("div", attrs={"class": "quick-facts-titulo"})
sao = city2.find("div", attrs={"class": "quick-facts-titulo"})
bar = city3.find("div", attrs={"class": "quick-facts-titulo"})
arearib = city1.find("ul", attrs={"class": "resultados-padrao"})
areasao = city2.find("ul", attrs={"class": "resultados-padrao"})
areabar = city3.find("ul", attrs={"class": "resultados-padrao"})
pibrib = city1.find("li", attrs={"data-grafico": "47001"})
pibsao = city2.find("li", attrs={"data-grafico": "47001"})
pibbar = city3.find("li", attrs={"data-grafico": "47001"})

rib= rib.find('h1')
ribresp = rib.text

sao = sao.find('h1')
saoresp = sao.text

bar = bar.find('h1')
barresp = bar.text

arearib = arearib.find("p", "ind-value")
arearibresp = arearib.text

areasao = areasao.find("p", "ind-value")
areasaoresp = areasao.text

areabar = areabar.find("p", "ind-value")
areabarresp = areabar.text

pibrib = pibrib.find("p", "ind-value")
pibribresp = pibrib.text

pibsao = pibsao.find("p", "ind-value")
pibsaoresp = pibsao.text

pibbar = pibbar.find("p", "ind-value")
pibbarresp = pibbar.text

# -------------------------------------------------------------------

planilha = openpyxl.Workbook()

page = planilha['Sheet']
page.title = 'Dados de cidades'

page.append(['CIDADE', 'ÁREA TERRITORIAL', 'POPULAÇÃO', 'PIB per capita'])
page.append([ribresp, arearibresp, 720.116, pibribresp])
page.append([saoresp, areasaoresp, 12.396372, pibsaoresp])
page.append([barresp, areabarresp, 33.537, pibbarresp])

page.column_dimensions['A'].width = 18
page.column_dimensions['B'].width = 20
page.column_dimensions['C'].width = 15
page.column_dimensions['D'].width = 19

estilo = Side(border_style='thin', color='000000')
borda = Border(top=estilo, bottom=estilo, left=estilo, right=estilo)

for x in range(1,5):
  page['A'+str(x)].border = borda
  page['B'+str(x)].border = borda
  page['C'+str(x)].border = borda
  page['D'+str(x)].border = borda

for y in range(1,5):
  page['A'+str(y)].alignment = Alignment(horizontal='center')
  page['B'+str(y)].alignment = Alignment(horizontal='center')
  page['C'+str(y)].alignment = Alignment(horizontal='center')
  page['D'+str(y)].alignment = Alignment(horizontal='center')

planilha.save('Dados de cidades.xlsx')

os.system("pause")