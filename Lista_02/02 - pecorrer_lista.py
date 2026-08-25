'''
Percorrendo uma lista
Considere a lista numeros = [7, 12, 5, 18, 3, 20]. Percorra a lista e exiba cada elemento em uma linha.
Depois, exiba somente os valores maiores que 10.
'''

numeros = [7, 12, 5, 18, 3, 20]

print("Lista completa: ")
for n in range(len(numeros)):
    print(numeros[n])
 
 
print("\nNúmeros somente > 10")    
for n in range(len(numeros)):
    if numeros[n] > 10:
        print(numeros[n])