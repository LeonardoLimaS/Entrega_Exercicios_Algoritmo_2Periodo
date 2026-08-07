#7. Leia 10 números e informe a soma e a média.

print("Calculo de soma e média de 10 números\n")

soma_media = 0
for i in range(1, 10+1):
    numero = int(input(f"Entre com o número para calcular a soma e a média {i}: "))
    soma_media = soma_media + numero
    media = soma_media / 10
        
print(f"Soma dos 10 numeros é : {soma_media}")
print(f"Média dos 10 numeros é : {media}")



