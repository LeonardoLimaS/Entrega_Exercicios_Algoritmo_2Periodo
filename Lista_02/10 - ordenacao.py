'''
Ordenação
Considere numeros = [18, 5, 12, 3, 20, 7, 9]. Exiba a lista original, depois a lista em ordem crescente e
finalmente em ordem decrescente. Utilize sort() ou sorted() e explique, em comentário no código, a
diferença entre eles.

'''


numeros = [18, 5, 12, 3, 20, 7, 9]
print(f"Lista original: {numeros}") 

# Ordenando em ordem crescente
numeros.sort()
print(f"Lista em ordem crescente: {numeros}")

# Ordenando em ordem decrescente
numeros.sort(reverse=True)
print(f"Lista em ordem decrescente: {numeros}")



# A diferença entre sort() e sorted() é que sort() modifica a lista original em si, 
# enquanto sorted() retorna uma nova lista ordenada, deixando a lista original inalterada. Exemplo:

numeros = [18, 5, 12, 3, 20, 7, 9]
numeros_ordenados = sorted(numeros)  # sorted() retorna uma nova lista ordenada
print(f"Lista original: {numeros}")
print(f"Lista ordenada: {numeros_ordenados}")


