import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

planilha = pd.read_excel("gasolina.xlsx")
imposto = planilha['IMPOSTO']
valor = planilha['VALOR']

# Grafico em pizza
plt.pie(valor, labels=imposto, autopct="%1.2f%%")

# Salva uma imagem do gráficp
plt.savefig("gasolina.png")

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('times', '', 16)
pdf.cell(0, 0, "Gráfico que detalha os imposto da gasolina")

# Cria uma linha
pdf.line(10, 15, 200, 15)

pdf.image(name="gasolina.png", x=0, y=20, w=200)
pdf.output("gasolina.pdf")

os.system("pause")