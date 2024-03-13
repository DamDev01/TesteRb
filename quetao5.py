def inverter_string(string):
    inverted_string = ''
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

# Teste
texto = "Python é incrível!"
texto_invertido = inverter_string(texto)
print("String original:", texto)
print("String invertida:", texto_invertido)
