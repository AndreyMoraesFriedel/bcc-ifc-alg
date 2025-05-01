# Início

# Definir função fatorial(n)
def fatorial(n):
    # Se n for igual a 0, então
    if n == 0:
        # Retornar 1 (caso base)
        return 1
    # Senão
    else:
        # Retornar n vezes o fatorial de (n - 1)
        return n * fatorial(n - 1)

# Obter valor de entrada (n)
n = int(input())

# Chamar a função e armazenar o resultado (fat = fatorial(n))
fat = fatorial(n)

# Mostrar o resultado do fatorial
print(f"Fatorial de {n}! = {fat}")

# Fim
