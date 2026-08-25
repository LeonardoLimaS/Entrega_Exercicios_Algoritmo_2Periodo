'''
Fatiamento
Considere valores = [10, 20, 30, 40, 50, 60, 70, 80]. Utilizando slicing, exiba: os quatro primeiros
elementos; os três últimos; os elementos das posições 2 a 5; e a lista invertida.
'''

valores = [10, 20, 30, 40, 50, 60, 70, 80]
# Quatro primeiros elementos
print(f"Quatro primeiros elementos: {valores[:4]}")

# Três últimos elementos
print(f"Três últimos elementos: {valores[-3:]}")

# Elementos das posições 2 a 5
print(f"Elementos das posições 2 a 5: {valores[2:6]}")

# Lista invertida
print(f"Lista invertida: {valores[::-1]}")