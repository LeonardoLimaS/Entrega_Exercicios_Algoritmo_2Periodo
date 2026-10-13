def soma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + soma_digitos(n // 10)


resultado = soma_digitos(123)
print(resultado) 

resultado = soma_digitos(456)
print(resultado)  

resultado = soma_digitos(789)
print(resultado)  