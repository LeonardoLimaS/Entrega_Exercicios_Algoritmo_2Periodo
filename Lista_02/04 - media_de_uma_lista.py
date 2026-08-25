'''
Média de uma lista
Considere notas = [7.5, 8.0, 6.0, 9.5, 5.5]. Calcule a média manualmente, percorrendo a lista. Ao final,
informe a média com duas casas decimais.
'''
notas = [7.5, 8.0, 6.0, 9.5, 5.5]
soma = 0
for n in range(len(notas)):
    soma += notas[n]
media = soma / len(notas)
print(f"A média das notas é: {media:.2f}")
