#1. Leia dois números e exiba a soma, subtração, multiplicação e divisão.

print("Digite dois números para efetuar as operações matemáticas, Soma, Subtração, Multiplicação e Divisão.")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

#Soma de dos números escolhidos
soma = numero1 + numero2
print("A soma de", numero1, "e", numero2, "é:", soma)


##Subtração dos números escolhidos
subtracao = numero1 - numero2
print("A subtração de", numero1, "e", numero2, "é:", subtracao)


###Multiplicação dos números escolhidos
multiplicacao = numero1 * numero2
print("A multiplicação de", numero1, "e", numero2, "é:", multiplicacao)


####Divisão dos números escolhidos
if numero1 != 0 and numero2 != 0:
    divisao = numero1 / numero2
    print("A divisão de", numero1, "e", numero2, "é:", divisao)  
else:
    print("Não é possível dividir por zero.")


