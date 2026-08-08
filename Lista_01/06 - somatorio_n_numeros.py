#6. Leia um número N e calcule a soma dos números de 1 até N


print("Calculo de somatório\n")
somatorio = int(input("Entre com o número para o somatório: "))

numero = 0
for i in range(1, somatorio+1):
    numero += i
    
print(f"Somatório de {somatorio} é : {numero}")