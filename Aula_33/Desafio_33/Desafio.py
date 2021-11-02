import os

lista = []

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")
cor = input("Digite sua cor favorita: ")
fruta = input("Digite sua fruta favorita: ")

for x in range(5):
  lista.append(nome)
  lista.append(idade)
  lista.append(altura)
  lista.append(cor)
  lista.append(fruta)
  print(lista[x])

os.system("pause")