import os, openpyxl

# Criando uma planilha
planilha = openpyxl.Workbook()

# Editando a primeira pagina da planilha
page_01 = planilha['Sheet']
page_01.title = 'pagina_01'

# Criando uma nova pagina na planilha
page_01 = planilha.create_sheet('pagina_02')

# Salvando a planilha mo computador
planilha.save('Teste_01.xlsx')

os.system("pause")