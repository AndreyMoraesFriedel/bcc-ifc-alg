# Início

# Definir função fibonacci(n)
def fibonacci(n):
    # Se n for igual a 0, então
    if n == 0:
        # Retornar 0 (caso base)
        return 0
    # Senão se n for igual a 1, então
    elif n == 1:
        # Retornar 1 (caso base)
        return 1
    # Senão
    else:
        # Retornar fibonacci(n-1) somado a fibonacci(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Obter quantidade de elementos da sequência (quantElementos)
quantElementos = int(input())

# Para cada número i de 0 até quantElementos - 1
for i in range(quantElementos):
    # Mostrar o valor de fibonacci(i) na mesma linha
    print(fibonacci(i), end=" ")

# Fim