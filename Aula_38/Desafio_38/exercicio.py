import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

planilha = pd.read_excel("GAS.xlsx")
imposto = planilha['IMPOSTO']
valor = planilha['VALOR']

plt.pie(valor, labels=imposto, autopct="%1.2f%%")

plt.savefig("gas.png")

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('times', '', 16)
pdf.cell(0, 0, "Gráfico que detalha os imposto do gás")

pdf.line(10, 15, 200, 15)

pdf.image(name="gas.png", x=0, y=20, w=200)
pdf.output("gas.pdf")

os.system("pause")