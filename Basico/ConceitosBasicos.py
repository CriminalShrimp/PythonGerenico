def variaveis():
  print("Variaveis são categorizadas em: ")
  print("0 - Boleano")
  print("1 - String")
  print("2 - Inteiro")
  print("3 - Float")
  print("4 - Voltar")
  while True:
    escolha = int(input("Escolha uma das opções acima: "))
    if escolha == 0:
      print("Esse tipo de variavel são somente False ou True, ou 0 e 1")
    elif escolha == 1:
      print("Esse tipo de variavel são caracteres, letras, palavras")
    elif escolha == 2:
      print("Esse tipo de variavel são numeros 0, 3, -4")
    elif escolha == 3:
      print("Esse tipo tambem são numeros. porem eles sao ponto flutuante como 3.14, 8.7")
    elif escolha == 4:
      clear()
      menu()
    else:
      print("Opção invalida")
      
def funcao():
  print("As peincipais funções são: ")
  print("0 - For")
  print("1 - While")
  print("2 - Range")
  print("3 - If,Else e Elif")
  print("4 - Voltar")
  while True:
    escolha = int(input("Escolha uma das opções acima: "))
    if escolha == 0:
      print("Até que a condição termine ele fica em um looping")
    elif escolha == 1:
      print("Enquanto um valor nao foi igual ao comparado ele segue em uma reptição")
    elif escolha == 2:
      print("Range(começo,fim,passo), sendo que nao precisa passar todos eles")
    elif escolha == 3:
      print("Se uma condição é atendida ele faz tal coisa, se-nao outra ou se-nao-entao(If, Else, Elif")
    elif escolha == 4:
      menu()
    else:
      print("Opção invalida")

def arquivo():
  print("Os modos para acesar o arquivo sao: ")
  print("r somente leitura, r+ leitura e escrita")
  print("w cria um arquvo para escrita, w+ cria para leitura tambem, se ja existir ele cira um novo")
  print("a leitura e escrita, a+ abre para atualizar o arquivo")
  menu()

def menu(): 
  print("Escolha umas das categorias que deseja: ")
  print("0 - Variaveis")
  print("1 - Funções")
  print("2 - Arquivos")
  print("3 - Sair")
  while True:
    escolha = int(input("Escolha uma das opções acima: "))
    if escolha == 0:
      variaveis()
    elif escolha == 1:
      funcao()
    elif escolha == 2:
      arquivo()
    elif escolha == 3:
      print("Ate mais")
      break
    else:
      print("Opção Invalida")


menu()