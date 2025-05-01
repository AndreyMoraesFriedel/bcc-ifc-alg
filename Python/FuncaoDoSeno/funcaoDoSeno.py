# Início

# Importar a função seno e conversão para radianos da biblioteca matemática
from math import sin, radians

# Definir função f(x)
def f(x):
    # Converter x para radianos (radiano = radians(x))
    radiano = radians(x)
    # Retornar o seno do ângulo em radianos
    return sin(radiano)

# Definir o deslocamento horizontal (delta = 98)
delta = 98

# Criar índice (i = 0)
i = 0

# Enquanto i for menor que 361
while i < 361:
    # Calcular o seno de i graus (seno = f(i))
    seno = f(i)
    # Mostrar o asterisco deslocado horizontalmente
    print(int(seno * delta + delta) * " " + "*")
    # Incrementar i
    i += 1

# Fim
