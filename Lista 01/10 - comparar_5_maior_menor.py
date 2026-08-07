#10. Desafio: Faça um programa que leia 5 números e informe o maior e o menor valor.

print("\nEntre com 5 números, para saber qual o maior entre eles")

#Variáveis para armazenar os números
numero_1 = 0
numero_2 = 0
numero_3 = 0
numero_4 = 0
numero_5 = 0
maior = 0

#Solicitando os números ao usuário
numero1 = int(input("Entre com o primeiro número: "))
numero2 = int(input("Entre com o segundo número: "))
numero3 = int(input("Entre com o terceiro número: "))
numero4 = int(input("Entre com o quarto número: "))
numero5 = int(input("Entre com o quinto número: "))


#Função 01
def maior_numero(numero1, numero2, numero3, numero4, numero5): 
    maior = numero1
    if numero2 > maior:
        maior = numero2
    if numero3 > maior:
        maior = numero3
    if numero4 > maior:
        maior = numero4
    if numero5 > maior:
        maior = numero5
    return maior

resultado = maior_numero(numero1, numero2, numero3, numero4, numero5)
print(f"O maior número é: {resultado}")



#Função 02
def _maior_numero(numero1, numero2, numero3, numero4, numero5):
    if numero1 > numero2 and numero1 > numero3 and numero1 > numero4 and numero1 > numero5:
        return numero1
    elif numero2 > numero1 and numero2 > numero3 and numero2 > numero4 and numero2 > numero5:
        return numero2
    elif numero3 > numero1 and numero3 > numero2 and numero3 > numero4 and numero3 > numero5:
        return numero3
    elif numero4 > numero1 and numero4 > numero2 and numero4 > numero3 and numero4 > numero5:
        return numero4
    else:
        return numero5


resultado = _maior_numero(numero1, numero2, numero3, numero4, numero5)
print(f"O maior número é: {resultado}")