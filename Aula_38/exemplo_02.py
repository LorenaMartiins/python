import os
from fpdf import FPDF

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()

# Adicionando uma fonte externa
# pdf.add_font('calibri', '', 'calibri.ttf', uni=True)

# Configurando a fonte
# Nome da fonte, formato(B, U, I ou ''), tamanho
pdf.set_font('times', '', 16)

# Adicionando texto no PDF
pdf.cell(0, 0, 'Olá mundo!!')

pdf.output('teste_02.pdf')

print("O PDF foi criado com sucesso!!")

os.system("pause")