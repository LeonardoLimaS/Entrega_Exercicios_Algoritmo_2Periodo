def Potencia_numero(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * Potencia_numero(base, expoente - 1)
    
    
resultado = Potencia_numero(2, 3)
print(resultado)

