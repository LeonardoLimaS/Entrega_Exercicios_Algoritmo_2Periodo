'''
Valores acima da média Leia 10 números reais e armazene-os em uma lista. Calcule a média e depois exiba somente os
valores que ficaram acima da média.
'''


# Lendo 10 números reais e armazenando em uma lista
numeros = []

for i in range(10):
    numero_entrada = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero_entrada)

# Calculando a média
media = sum(numeros) / len(numeros)

# Exibindo os valores acima da média
print(f"Valores acima da média ({media:.2f}):")
for n in numeros:
    if n > media:
        print(n)
