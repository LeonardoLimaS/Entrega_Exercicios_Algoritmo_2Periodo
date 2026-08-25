'''
Frequência dos elementos
Dada uma lista de números inteiros, informe quantas vezes cada valor aparece. Exemplo: para [2, 3, 2,
5, 3, 2], a saída deve indicar que 2 aparece 3 vezes, 3 aparece 2 vezes e 5 aparece 1 vez.
'''

numeros = [2, 3, 2, 5, 3, 2]
frequencia = {}

for n in numeros:
    if n in frequencia:
        frequencia[n] += 1
    else:
        frequencia[n] = 1

for valor, quantidade in frequencia.items():
    print(f"O valor {valor} aparece {quantidade} vezes.")