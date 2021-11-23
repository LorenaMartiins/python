import os, openpyxl

planilha = openpyxl.Workbook()

page = planilha['Sheet']
page.title = 'Estudo'

# Adicionando informações na planilha
page.append(['NOME', 'IDADE', 'CIDADE'])
page.append(['Jubileu', 45, 'Bauru'])
page.append(['Ana Julia', 27, 'São Paulo'])
page.append(['Victor', 35, 'Rio de Janeiro'])

# Editando o tamanho da coluna
page.column_dimensions['A'].width = 20
page.column_dimensions['B'].width = 6
page.column_dimensions['C'].width = 20

planilha.save('Nomes.xlsx')

os.system("pause")