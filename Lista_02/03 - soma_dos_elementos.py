'''
Soma dos elementos
Crie uma lista com 8 números inteiros. Calcule e exiba a soma de todos os elementos sem utilizar a
função sum().
'''

numeros = [1, 2, 23, 4, 5, 6, 7, 10]

soma = 0
for n in range(len(numeros)):
    soma += numeros[n]
print(f"A soma dos elementos é: {soma}")