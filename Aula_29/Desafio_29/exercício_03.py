#corrigido

import os

codigo = input("Digite aqui o código do produto:")
nome = input("Nome do produto:")
quantidade = int(input("Quantidade do produto:"))
preço = float(input("Preço do produto:"))

resp = quantidade * preço

print("----------------")
print("Código:",codigo)
print("Nome:",nome)
print("Quantidade:",quantidade)
print("PERÇO: R$",preço)
print("----------------")
print("Total: R$",resp)
print("----------------")

os.system("pause")