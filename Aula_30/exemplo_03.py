import os

resp = input("CPU - Olá! Tudo bem com você?")

if resp == "sim" or resp == "Sim":
    print("CPU - Nossa que legal :D")
elif resp == "não" or resp == "Não" or resp == "não" or resp == "Não":
    print("CPU - Oh! Não fique trsite amiguinho!")
else:
    print("CPU - Me desculpe! Não entendi sua resposta!")

os.system("pause")