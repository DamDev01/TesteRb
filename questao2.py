numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

a, b = 0, 1
while b < numero:
    a, b = b, a + b

if b == numero:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
