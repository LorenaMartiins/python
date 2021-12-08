import os
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()
pdf.set_font('times', '', 16)

# Variavel do texto
texto = "Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991."

# Adiciona um texto no PDF
pdf.multi_cell(w=0, h=8, txt=texto, align='J')

# Adiciona uma imagem no PDF
pdf.image(name='logo.png', x=65, y=50, w=75)

pdf.output('teste_03.pdf')

print("O PDF foi criado com sucesso!!")

os.system("pause")