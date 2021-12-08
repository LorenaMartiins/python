import os
from fpdf import FPDF

# Criando um PDF
pdf = FPDF('P', 'mm', 'A4')
# 'P' deixa o PDF na vertical
# 'L' deixa o PDF na horizontal
# Medidas do documento = mm, cm, in
# Formato de documento = A3, A4, A5, Latter e Legal.

# Criando uma página para o PDF
pdf.add_page()

# Salvando o arquivo PDF
pdf.output('teste_01.pdf')

print("O PDF doi criado com sucesso!!")

os.system("pause")