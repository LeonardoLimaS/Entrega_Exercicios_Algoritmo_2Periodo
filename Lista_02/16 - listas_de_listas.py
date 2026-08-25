'''
Lista de listas
Crie uma matriz 3x3 utilizando listas de listas. Exiba todos os elementos, a soma de todos os valores e
a soma de cada linha.
'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Exibindo todos os elementos
print("Elementos da matriz:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # Quebra de linha após cada linha da matriz

# Soma de todos os valores
soma_total = sum(sum(linha) for linha in matriz)
print(f"Soma de todos os valores: {soma_total}")

# Soma de cada linha
print("Soma de cada linha:")
for i, linha in enumerate(matriz):
    soma_linha = sum(linha)
    print(f"Linha {i+1}: {soma_linha}")