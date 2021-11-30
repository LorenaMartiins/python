import os
import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel('Alunos.xlsx')

# Titulo para o grafico
plt.title("Exemplo de gráfico")

# Adiciona legendas no eixo X e Y
# plt.xlabel("Exemplo X")
# plt.ylabel("Exemplo Y")

# Criando um gráfico em forma de linha
# plt.plot(planilha['IDADE'])

# Criando um gráfico em forma de barra
# plt.hist (planilha['IDADE'], bins=20)

# Criando um gráfico em forma de pizza
plt.pie(planilha['IDADE'], labels=planilha['NOME'])

plt.show()

os.system("pause")