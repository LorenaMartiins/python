import os

print("-------------------------------")
print("1 - Semaforo verde")
print("2 - Semaforo laranja")
print("3 - Semaforo vermelho")
print("-------------------------------")
semaforo = int(input("Escolha uma opção:"))

if semaforo == 3:
    print("Pare e espere!")
elif semaforo == 2:
    print("Atenção!")
elif semaforo == 2:
    print("Siga em frente!")
else:
    print("Valor errado!")

os.system("pause")