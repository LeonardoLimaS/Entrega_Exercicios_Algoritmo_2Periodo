#9. Crie uma função que receba dois números e retorne o maior deles.

print("\nFunção que retorna o maior número entre dois números.")
print("Entre com dois números para comparar.\n")
numero1 = int(input("Entre com o primeiro número: "))
numero2 = int(input("Entre com o segundo número: "))

def maior_numero(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2
    
maior = maior_numero(numero1, numero2)
print(f"O maior número é: {maior}")