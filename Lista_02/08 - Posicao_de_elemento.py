'''
Posição de um elemento
Considere nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]. Solicite um nome ao usuário e
informe a posição em que ele aparece. Caso não exista, informe que o nome não foi encontrado.
'''

nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
nome_pesquisa = input("Digite um nome para pesquisar: ")
encontrado = False
for i, nome in enumerate(nomes):
    if nome == nome_pesquisa:
        print(f"O nome {nome_pesquisa} está na posição {i}.")
        encontrado = True
        break
if not encontrado:
    print(f"O nome {nome_pesquisa} não foi encontrado.")   
    
