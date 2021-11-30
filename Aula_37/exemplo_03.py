import os
import pandas as pd
import matplotlib.pyplot as plt

# Abrimos a planilha Dolar.xlsx
planilha = pd.read_excel('Dolar.xlsx')
# Pegamos informação da coluna VALOR
dolar = planilha['VALOR']

plt.title("Cotação do Dolár - Novembro")

plt.ylabel("Valor do dolar")
plt.xlabel("Dias do mês")

# Gera o gráfico com a cotação do dólar
plt.plot(dolar, marker='D', linestyle='dotted', color='#000000')

plt.grid()

plt.show()

os.system("pause")