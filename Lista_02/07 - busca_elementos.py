'''
Busca de um elemento
Leia 8 números e armazene-os em uma lista. Depois, solicite ao usuário um número para pesquisar.
Informe se ele está ou não na lista. Não utilize index() para realizar a busca.
'''

numeros = []
for i in range(8):
    numero_entrada = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero_entrada)

pesquisa = int(input("Digite o número a ser pesquisado: "))

encontrado = False
for n in numeros:
    if n == pesquisa:
        encontrado = True
        break

if encontrado:
    print(f"O número {pesquisa} está na lista.")
else:
    print(f"O número {pesquisa} não está na lista.")