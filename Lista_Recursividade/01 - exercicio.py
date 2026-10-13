def Mdc(a,b):
    if b == 0:
        return a
    else:
        return Mdc(b, a % b)
    

resultado = Mdc(12, 16)
print(resultado)