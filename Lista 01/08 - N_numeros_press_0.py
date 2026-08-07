#8. Leia vários números até que o usuário digite 0. Ao final, informe a soma dos valores digitados.


print("Calculo de soma de vários números, digite 0 para parar.\n")

soma = 0
contador = 1
numero = int(input(f"Entre com o número para calcular a soma {contador}: "))

while numero != 0:
    contador += 1
    numero = int(input(f"Entre com o número para calcular a soma {contador}: "))
    soma = soma + numero
    if numero == 0:
        break
print(f"Soma dos numeros é : {soma}")

