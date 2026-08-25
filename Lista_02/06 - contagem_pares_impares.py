'''
Contagem de pares e ímpares
Lista de Exercícios — Listas em Python | Página 2
Dada uma lista com 10 números inteiros, conte quantos são pares e quantos são ímpares. Exiba as
duas quantidades ao final.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")