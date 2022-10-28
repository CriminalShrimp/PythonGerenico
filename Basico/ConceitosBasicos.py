print("Variaveis são categorizadas em: ")
print("0 - Boleano")
print("1 - String")
print("2 - Inteiro")
print("3 - Float")
print("4 - Sair")
while True:
  escolha = input("Escolha uma das opções acima: ")
  if escolha == "0":
    print("Esse tipo de variavel pode ser somente True ou False, ou 1 e 0")
  if escolha == "1":
    print("Esse tipo de variavel são caracteres, letras, palavras")
  if escolha == "2":
    print("Esse tipo de variavel são numeros 0, 3, -4")
  if escolha == "3":
    print("Esse tipo tambem são numeros. porem eles sao ponto flutuante como 3.14, 8.7")
  if escolha == "4":
    print("Ate mais")
    break