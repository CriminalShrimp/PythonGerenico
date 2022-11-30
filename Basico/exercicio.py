idade = int(input("Digite sua idade: "))
if idade < 18:
   print("Menor de idade")
else: 
  print("Voce é maior de idade")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
total = (nota1 + nota2)/2
if total >= 6.0:
  print("Aprovado ")
else:
  print("Reporavado")
from math import sqrt
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
delta = b **2 - 4 * a * c
if delta < 0: 
  print("delta é negativo")
else:
  raiz_delta = sqrt(delta)
  x1 = (-b + raiz_delta)/2*a
  x2 = (-b - raiz_delta)/2*a
  print("As raízes são", x1, "e", x2)
lista = []
for i in range(0,3,1):
  lista.append(int(input("Digite um valor ")))
print(sorted(lista))
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um outro numero: "))
sinal = int(input("Digite um operador logico: "))
if sinal == "*" or ".":
  print(a*b)
elif sinal == "-":
  print(a-b)
elif sinal == "+":
  print(a+b)
elif sinal == "/":
  print(a/b)
elif sinal == "^":
  print(a**b)