import os
import pandas as pd
import matplotlib.pyplot as plt

# Abrindo a planilha com a biblioteca pandas
planilha = pd.read_excel("Alunos.xlsx")

print("1 - Mostra a planilha")
print("2 - Mostra uma coluna")
print("3 - Mostra um valor")
opc = int(input("Escolha a opcao: "))

if opc == 1:
  # Mostrando a planilha completa
  print(planilha)
elif opc == 2:
  # Mostrando uma coluna
  print(planilha['NOME'])
else:
  # Mostrar um valor
  print(planilha['NOME'][0])

os.system("pause")