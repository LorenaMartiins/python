import os
import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel('Cotacao dolar.xlsx')
dolar = planilha['VALOR']

plt.title("Cotação do Dolár - Jan/Nov")

plt.ylabel("Valor do dolar")
plt.xlabel("Mês")

plt.plot(dolar, marker='D', linestyle='dotted', color='#696969')

plt.show()

os.system("pause")