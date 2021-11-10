import os

def bis(n1, n2, n3, n4, n5):
  calc = (n1 + n2 + n3 + n4 + n5)/5
  if calc >= 6:
    print("Aluno aprovado!\nnota: ", calc)
  else:
    print("Aluno reprovado!\nnota: ", calc)
def tri(n1, n2, n3):
  calc = (n1 + n2 + n3)/3
  if calc >= 6:
    print("Aluno aprovado!\nnota: ", calc)
  else:
    print("Aluno reprovado!\nnota: ", calc)
def sem(n1, n2):
  calc = (n1 + n2)/2
  if calc >= 6:
    print("Aluno aprovado!\nnota: ", calc)
  else:
    print("Aluno reprovado!\nnota: ", calc)

print("---------------------")
print("1 - Bimestre")
print("2 - Trimestre")
print("3 - Semestre")
print("---------------------")
opc = int(input("Digite a opção: "))

if opc == 1:
  n1 = int(input("Digite a primeira nota:"))
  n2 = int(input("Digite a segunda nota:"))
  n3 = int(input("Digite a terceira nota:"))
  n4 = int(input("Digite a quarta nota:"))
  n5 = int(input("Digite a quinta nota:"))
  bis(n1, n2, n3, n4, n5)
elif opc == 2:
  n1 = int(input("Digite a primeira nota:"))
  n2 = int(input("Digite a segunda nota:"))
  n3 = int(input("Digite a terceira nota:"))
  tri(n1, n2, n3)
elif opc == 3:
  n1 = int(input("Digite a primeira nota:"))
  n2 = int(input("Digite a segunda nota:"))
  sem(n1, n2)
else:
  print("Erro na opção!")
  
print("---------------------")

os.system("pause")