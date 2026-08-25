'''
Segundo maior valor.
Dada uma lista de números inteiros, encontre o segundo maior valor distinto sem utilizar sort().
Considere que a lista possui pelo menos dois valores distintos.
'''

numeros = [10, 5, 8, 12, 3, 7]
# Inicializando o maior e o segundo maior com valores mínimos
maior = float('-inf') #inicializa o maior com o menor valor possível, assim qualquer número será maior que ele. (-inf) é uma abreviação para "negative infinity"
segundo_maior = float('-inf') # -inf significa que é o menor valor possível, assim qualquer número será maior que ele.

for n in numeros:
    if n > maior:
        segundo_maior = maior
        maior = n
    elif n > segundo_maior and n != maior:
        segundo_maior = n

print(f"O segundo maior valor é: {segundo_maior}")