# Início

# Obter os valores de entrada em uma única linha e dividir em lista (values)
values = input().split(' ')

# Converter os valores para inteiro (a, b, c)
a = int(values[0])
b = int(values[1])
c = int(values[2])

# Calcular o maior entre a e b (maiorAB = (a + b + |a - b|) // 2)
maiorAB = (a + b + abs(a - b)) // 2

# Calcular o maior entre maiorAB e c (maiorABC = (c + maiorAB + |c - maiorAB|) // 2)
maiorABC = (c + maiorAB + abs(c - maiorAB)) // 2

# Mostrar o resultado formatado como "X eh o maior"
print(f"{maiorABC} eh o maior")

# Fim
