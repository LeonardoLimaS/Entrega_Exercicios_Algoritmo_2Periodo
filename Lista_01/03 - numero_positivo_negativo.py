#3. Leia um número e informe se ele é positivo, negativo ou zero.

numero = float(input("Digite um numero para saber se ele é positivo, negativo ou zero: "))

if numero > 0:
    print(f"Número digitado {numero} é positivo")
elif numero < 0:
    print(f"Número digitado {numero} é negativo")
elif numero == 0:
    print(f"Número digitado {numero} é Zero")
    
