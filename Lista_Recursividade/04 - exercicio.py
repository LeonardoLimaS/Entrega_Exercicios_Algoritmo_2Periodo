def verificar_palindromo(s):
    s = s.replace(" ", "").lower()
    
    if len(s) <= 1:
        return True
        
    if s[0] != s[-1]:
        return False
        
    return verificar_palindromo(s[1:-1])



resultado = verificar_palindromo("arara")
print(resultado)
