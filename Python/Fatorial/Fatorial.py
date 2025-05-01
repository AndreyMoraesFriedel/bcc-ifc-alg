# Início

# Obter valor de entrada (n)
n = int(input())

# Criar acumulador para o fatorial (fatorial = 1)
fatorial = 1

# Se n <= 1, então
if n <= 1:
    # Manter fatorial igual a 1
    fatorial = 1
# Senão
else:
    # Criar índice (i = 1)
    i = 1
    # Enquanto i <= n
    while i <= n:
        # Multiplicar fatorial por i
        fatorial *= i
        # Incrementar i
        i += 1

# Mostrar resultado do fatorial
print(f"Fatorial de {n}! = {fatorial}")

# Fim