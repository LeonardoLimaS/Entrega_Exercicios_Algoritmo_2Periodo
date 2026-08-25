'''
Inserção e remoção
Crie uma lista inicialmente vazia. Leia 5 números e utilize append() para inseri-los. Depois, solicite um
número ao usuário e remova sua primeira ocorrência, caso exista. Exiba a lista antes e depois da
remoção.

'''

numeros = []
for _ in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print(f"Lista antes da remoção: {numeros}")

numero_removido = int(input("Digite o número a ser removido: "))

if numero_removido in numeros:
    numeros.remove(numero_removido)
    print(f"Lista depois da remoção: {numeros}")
else:
    print("O número não foi encontrado na lista.")