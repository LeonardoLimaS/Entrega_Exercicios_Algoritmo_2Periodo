'''
Compreensão de listas
Considere numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Crie, utilizando compreensão de listas: uma lista
com os quadrados; uma lista somente com os pares; e uma lista contendo apenas os números maiores
que 5.
'''

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista com os quadrados
quadrados = [n**2 for n in numeros]
print("Lista com os quadrados:", quadrados)

# Lista somente com os pares
pares = [n for n in numeros if n % 2 == 0]
print("Lista somente com os pares:", pares)

# Lista contendo apenas os números maiores que 5
maiores_que_5 = [n for n in numeros if n > 5]
print("Lista contendo apenas os números maiores que 5:", maiores_que_5)

