'''
Maior e menor valor
Crie uma lista de números inteiros e determine o maior e o menor elemento sem utilizar max() ou
min().
'''

numeros = [7, 12, 5, 18, 3, 20]
maior = numeros[0]
menor = numeros[0]

for n in range(1, len(numeros)):
    if numeros[n] > maior:
        maior = numeros[n]
    if numeros[n] < menor:
        menor = numeros[n]

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")