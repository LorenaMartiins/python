import os, openpyxl
from openpyxl.styles import Border, Side, Alignment

planilha = openpyxl.Workbook()

page = planilha['Sheet']
page.title = 'Produtos'

page.append(['NOME', 'QUANTIDADE', 'PREÇO'])
page.append(['Leite', 3, 'R$ 5.30'])
page.append(['Queijo', 2, 'R$ 6.00'])
page.append(['Bolacha', 2, 'R$2.99'])

page.column_dimensions['A'].width = 20
page.column_dimensions['B'].width = 13
page.column_dimensions['C'].width = 10

# Definindo o estilo da borda
estilo = Side(border_style='thin', color='000000')

# Aplicando a borda em todos os lados da célula
borda = Border(top=estilo, bottom=estilo, left=estilo, right=estilo)

# Desenha a borda nas colunas da tabela
for x in range(1,5):
  page['A'+str(x)].border = borda
  page['B'+str(x)].border = borda
  page['C'+str(x)].border = borda

# Alinhando o texto 
for y in range(1,5):
  page['A'+str(y)].alignment = Alignment(horizontal='distributed')
  page['B'+str(y)].alignment = Alignment(horizontal='distributed')
  page['C'+str(y)].alignment = Alignment(horizontal='distributed')
  
planilha.save('Produtos.xlsx')

os.system("pause")