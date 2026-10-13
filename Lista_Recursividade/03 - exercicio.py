def inverter_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + inverter_string(s[:-1])

resultado = inverter_string("python")
print(resultado)
