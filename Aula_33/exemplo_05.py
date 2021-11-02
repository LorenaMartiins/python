import os

lista = []

# cadastrando 5 nomes em uma lista
for x in range(5):
  nome = input("Digite um nome: ")
  lista.append(nome)

print('---------------------')

# mostrando valores da lista
for y in range(len(lista)):
  print(lista[y])

os.system("pause")