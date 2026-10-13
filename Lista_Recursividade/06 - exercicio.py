def encontrar_anagramas(string):
    if len(string) <= 1:
        return [string]
    
    anagramas = []
    for i, letra in enumerate(string):
        restante = string[:i] + string[i+1:]
        for anagrama in encontrar_anagramas(restante):
            anagramas.append(letra + anagrama)
    
    return anagramas


resultado = encontrar_anagramas("abc")
print(resultado)
