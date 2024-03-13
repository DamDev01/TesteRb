# Sequências
sequences = {
    'a': [1, 3, 5, 7],
    'b': [2, 4, 8, 16, 32, 64],
    'c': [0, 1, 4, 9, 16, 25, 36],
    'd': [4, 16, 36, 64],
    'e': [1, 1, 2, 3, 5, 8],
    'f': [2, 10, 12, 16, 17, 18, 19]
}

# Próximos elementos
next_elements = {
    'a': 9,
    'b': 128,
    'c': 49,
    'd': 100,
    'e': 13,
    'f': 20
}

# Imprimir próximo elemento de cada sequência
for key in sequences:
    print(f'Próximo elemento da sequência {key}: {next_elements[key]}')
