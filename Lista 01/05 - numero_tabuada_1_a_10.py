#5. Leia um número inteiro e mostre sua tabuada de 1 a 10

print("Tabuada")
numero = int(input("Digite um numero para mostrar a tabuada completa: "))

for i in range(0, numero+1):
    tabuada = numero * i
    print(f"{numero} x {i} = {tabuada}")
